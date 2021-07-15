export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const myObj = { status: 200, body: 'Success' };
      resolve(myObj);
    } else {
      const errorObj = 'The fake API is not working currently';
      reject(new Error(errorObj));
    }
  });
}
