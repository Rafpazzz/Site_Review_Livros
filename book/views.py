import csv
import io

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from accounts.views import is_system_admin
from reviews.models import Review
from .models import Books

REVIEWS_PER_PAGE = 10


def _build_books_pdf(books):
    buffer = io.BytesIO()
    document = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        pageCompression=0,
        rightMargin=24,
        leftMargin=24,
        topMargin=24,
        bottomMargin=24,
        title='Livros',
    )
    styles = getSampleStyleSheet()
    normal_style = styles['BodyText']
    table_data = [['ID', 'Titulo', 'Autor', 'Editora', 'Ano']]

    for book in books:
        table_data.append([
            str(book.id),
            Paragraph(book.titulo, normal_style),
            Paragraph(book.autor, normal_style),
            Paragraph(book.editora, normal_style),
            str(book.ano_publicacao),
        ])

    table = Table(table_data, repeatRows=1, colWidths=[42, 230, 170, 170, 70])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#12395b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    document.build([
        Paragraph('Livros', styles['Title']),
        Spacer(1, 12),
        table,
    ])
    return buffer.getvalue()

def all_books(request):
    books = Books.objects.all()
    return render(request, 'all_books.html', {'books': books})


def search_book(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    query = request.GET.get('q', '').strip()
    if query:
        books = Books.objects.filter(titulo__icontains=query)
    else:
        books = Books.objects.all()
    return render(request, 'search_book.html', {'books': books, 'query': query})


@user_passes_test(is_system_admin, login_url='login')
def export_books_csv(request):
    books = Books.objects.all().order_by('titulo')

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="livros.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'titulo', 'autor', 'editora', 'ano_publicacao', 'resumo'])

    for book in books:
        writer.writerow([book.id, book.titulo, book.autor, book.editora, book.ano_publicacao, book.resumo])

    return response


@user_passes_test(is_system_admin, login_url='login')
def export_books_pdf(request):
    books = Books.objects.all().order_by('titulo')

    response = HttpResponse(_build_books_pdf(books), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="livros.pdf"'
    return response


def detalhes(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    book = get_object_or_404(Books, pk=id)
    reviews = (
        Review.objects
        .filter(book=book)
        .select_related("autor")
        .order_by("-created_at")
    )
    paginator = Paginator(reviews, REVIEWS_PER_PAGE)
    reviews_page = paginator.get_page(request.GET.get("page"))
    reviews_page_range = paginator.get_elided_page_range(
        number=reviews_page.number,
        on_each_side=1,
        on_ends=1,
    )

    return render(
        request,
        'detalhes.html',
        {
            'book': book,
            'reviews_page': reviews_page,
            'reviews_count': paginator.count,
            'reviews_page_range': reviews_page_range,
        },
    )
