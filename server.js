const axios = require('axios');

const urlToAccess = 'https://naman-portfolio-3.onrender.com/index.html'; // Replace with the URL you want to access
const retryInterval = 40000; // Retry interval in milliseconds (5 seconds in this case)

async function accessWebsite(url) {
    try {
        const response = await axios.get(url);
        console.log(`Successfully accessed ${url}. Status: ${response.status}`);
        return true; // Return true if successfully accessed
    } catch (error) {
        console.error(`Error accessing ${url}:`, error.message);
        return false; // Return false if error occurred
    }
}

async function continuouslyAccessWebsite(url, interval) {
    setInterval(async () => {
        console.log(`Attempting to access ${url}...`);
        const success = await accessWebsite(url);
        if (success) {
            console.log(`Successfully accessed ${url}. Stopping retries.`);
            clearInterval(this); // Stop further retries if successful
        }
    }, interval);
}

// Start accessing the website continuously
continuouslyAccessWebsite(urlToAccess, retryInterval);
