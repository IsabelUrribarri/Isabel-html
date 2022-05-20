var myHeaders = new Headers();
myHeaders.append("apikey", "13MHSPiFpdwWoay3HQRhEE1wdkXK8USY");

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

fetch("https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=USD&amount=10", requestOptions)
  .then(response => response.json())
    .then(data => {

        // Get rate from data
        const rate = data.result;

        // Display message on the screen
        document.querySelector('body').innerHTML = rate;//`1 USD is equal to ${rate.toFixed(3)} EUR.`;
    });