import type { Arguments, CommandBuilder } from 'yargs';
import * as emoji from 'node-emoji';
type Options = {
    name: string;
    upper: boolean | undefined;
};

export const command: string = 'greet <name>';
export const desc: string = 'Greet <name> with Hello';

export const builder: CommandBuilder<Options, Options> = (yargs) =>
    yargs
        .options({
          upper: { type: 'boolean' },
        })
        .positional('name', { type: 'string', demandOption: true });

export const handler = (argv: Arguments<Options>): void => {
    const { name, upper } = argv;
    const coffee = emoji.emojify('I :heart: :coffee:!');
    emoji.get('coffee')
    const greeting = `Hello, ${name}! ${coffee}`;
    process.stdout.write(upper ? greeting.toUpperCase() : greeting);
    process.exit(0)
};

