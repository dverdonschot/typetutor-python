"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.handler = exports.builder = exports.desc = exports.command = void 0;
const emoji = __importStar(require("node-emoji"));
exports.command = 'greet <name>';
exports.desc = 'Greet <name> with Hello';
const builder = (yargs) => yargs
    .options({
    upper: { type: 'boolean' },
})
    .positional('name', { type: 'string', demandOption: true });
exports.builder = builder;
const handler = (argv) => {
    const { name, upper } = argv;
    const coffee = emoji.emojify('I :heart: :coffee:!');
    emoji.get('coffee');
    const greeting = `Hello, ${name}! ${coffee}`;
    process.stdout.write(upper ? greeting.toUpperCase() : greeting);
    process.exit(0);
};
exports.handler = handler;
