import { Arguments, CommandBuilder, string } from 'yargs';
import * as emoji from 'node-emoji';
import { stringify } from 'querystring';
import { Readline } from 'readline/promises';

type Options = {
    letters: string;
    upper: boolean | undefined;
};

export const command: string = 'letters <letters>';
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

    var keypress = require('keypress');
 
    // make `process.stdin` begin emitting "keypress" events
    keypress(process.stdin);
     
    // listen for the "keypress" event
    process.stdin.on('keypress', function (ch, key) {
      console.log('got "keypress"', key.name);
      if (key && key.ctrl && key.name == 'c') {
        process.stdin.pause();
      }
    });
     
    process.stdin.setRawMode(true);
    process.stdin.resume();

};








