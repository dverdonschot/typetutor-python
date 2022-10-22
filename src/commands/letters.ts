import { Arguments, CommandBuilder, string } from 'yargs';
import * as emoji from 'node-emoji';
import { getQuote } from '../functions/fetchQuote'
import { stringify } from 'querystring';

type Options = {
    letters: string;
    upper: boolean | undefined;
};

export const command: string = 'type <letters>';
export const desc: string = 'letters that you want to learn typing';

export const builder: CommandBuilder<Options, Options> = (yargs) =>
    yargs
        .options({
          upper: { type: 'boolean' },
        })
        .positional('letters', { type: 'string', demandOption: true });

export const handler = (argv: Arguments<Options>): void => {
    const { letters, upper } = argv;
    const horse = emoji.emojify('I :heart: :horse:!');
    emoji.get('father')
    const greeting = `Hello, ${letters}! ${horse}`;
    process.stdout.write(upper ? greeting.toUpperCase() : greeting);
    getQuote().then.toString
};



//export const quote_getter: Promise<void> = getQuote();
//process.stdout.write(quote_getter)






