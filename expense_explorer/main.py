import click
import logging


@click.group()
def cli():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    pass


@cli.command()
@click.option('-i', '--input_file', help='Input file to convert', required=True)
@click.option('-o', '--output_file', help='Output file after conversion', required=True)
@click.option('-c', '--converter', help='The converter to use on the input file', required=True)
def convert(input_file, output_file, converter):
    log = logging.getLogger()
    log.info(f"Input file: {input_file}, Output file: {output_file}, Converter: {converter}")
