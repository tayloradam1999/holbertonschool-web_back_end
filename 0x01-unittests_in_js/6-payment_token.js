// if success is true, returns new promise and is tested by 6-payment_token.test.js
function getPaymentTokenFromAPI(success) {
	if (success) {
		return new Promise ((Resolve, reject) => {
			Resolve({data: 'Successful response from the API'});
		});
	}
}

module.exports = getPaymentTokenFromAPI;