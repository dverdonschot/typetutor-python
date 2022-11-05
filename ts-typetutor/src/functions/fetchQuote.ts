import axios from 'axios';

    
interface iRandomQuote {
    maxLength: number;
    minLength: number;
    tags: string;
    author: string;
    authorId: string;
}


//const axiosRequest = require('axios');

export async function getQuote() {
    let response = await axios.get('https://www.boredapi.com/api/activity');
    console.log(`You could ${response.data.activity}`);
}

