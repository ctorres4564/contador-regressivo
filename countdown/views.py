from django.shortcuts import render
from datetime import datetime


def countdown_view(request):
    # Inicializar variáveis padrão
    event_date = None
    total_seconds = 0
    error_message = None

    # Verificar se uma data foi fornecida pelo formulário
    event_date_str = request.GET.get("event_date")

    if event_date_str:
        try:
            # Converter a data fornecida para um objeto datetime
            event_date = datetime.strptime(event_date_str, "%Y-%m-%dT%H:%M")
            current_date = datetime.now()

            # Verificar se a data é futura
            if event_date <= current_date:
                error_message = "A data do evento deve ser no futuro."
            else:
                # Calcular o tempo restante
                time_remaining = event_date - current_date
                total_seconds = time_remaining.total_seconds()

        except ValueError:
            # Tratar erros de formatação da data
            error_message = "Formato de data inválido. Use o formato YYYY-MM-DDTHH:MM."

    # Passe os dados para o template
    context = {
        "event_date": event_date,
        "total_seconds": total_seconds,
        "error_message": error_message,  # Adiciona mensagem de erro, se houver
    }
    return render(request, "countdown/countdown.html", context)


def home_view(request):
    return render(request, "countdown/home.html")
