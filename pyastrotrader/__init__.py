from pyastrotrader.calculate import load_config, generate_chart
from pyastrotrader.transits import calculate_aspects
from pyastrotrader.transits import calculate_transits
from .config import check_input


def show_usage():
    pass


def calculate_chart(input_json):
    input_data = check_input(input_json)
    config = load_config(input_data)
    output = generate_chart(config, input_data)
    return output


__all__ = ['calculate_transits', 'calculate_chart', 'calculate_aspects']
