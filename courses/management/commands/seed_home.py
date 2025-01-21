from django.core.management.base import BaseCommand
from courses.models import Home  # Importa o modelo Home da aplicação courses.models

class Command(BaseCommand):  # Corrige o nome da classe para "Command"
    # Mensagem de ajuda que descreve o propósito do comando
    help = "Seed para cadastrar registro na tabela Home"

    # O método `handle` é o ponto de entrada para comandos personalizados
    def handle(self, *args, **kwargs):
        # Dados a serem cadastrados na tabela Home
        home = {
            'title': 'Bem-vindo à Academia de Infraestrutura!',
            'subtitle': 'Fortalecendo Seu Potencial com Treinamentos de Alto Desempenho e Tecnologia de Ponta.',
            'text_btn': 'Explore Nossos Planos',
            'link_btn': 'https://infraacademy.com.br',
            'title_topics': 'Por Que Treinar Conosco?',
            'subtitle_topics': 'Cuidar da saúde e bem-estar é essencial para uma vida equilibrada e feliz. Treinar na nossa academia ajuda você a:',
            'title_topic_one': 'Construa uma Base Sólida para o Sucesso',
            'description_topic_one': 'Melhore sua saúde física e mental com treinos que se adaptam ao seu estilo de vida.',
            'title_topic_two': 'Alcançar Resultados',
            'description_topic_two': 'Conte com profissionais qualificados para ajudar você a atingir suas metas de forma eficiente.',
            'title_topic_three': 'Ganhar Confiança',
            'description_topic_three': 'Melhore sua autoestima e bem-estar geral com um corpo saudável e ativo.',
        }

        # Atualiza o registro existente ou cria um novo com base no título
        Home.objects.update_or_create(
            title=home['title'],  # Critério de busca: título
            defaults=home  # Valores padrão para criar ou atualizar
        )

        # Exibe uma mensagem de sucesso no terminal
        self.stdout.write(self.style.SUCCESS('Home cadastrada com sucesso!'))