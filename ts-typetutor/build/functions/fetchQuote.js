"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getQuote = void 0;
const axios_1 = __importDefault(require("axios"));
//const axiosRequest = require('axios');
async function getQuote() {
    let response = await axios_1.default.get('https://www.boredapi.com/api/activity');
    console.log(`You could ${response.data.activity}`);
}
exports.getQuote = getQuote;
