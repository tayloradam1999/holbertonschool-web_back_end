export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      const myObj = { status: 200, body: 'Success' };
      resolve(myObj);
    } else {
        const errorObj = "The fake API is not working currently";
        reject(errorObj);
    }
  })
};
