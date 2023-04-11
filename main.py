from cli import Cli

def main():
    cli = Cli()
    running = True

    while running:
       running = cli.start()

main()

print('===Goodbye!===')
