// Create kue queue
const kue = require('kue');
const queue = kue.createQueue();

// function to log data to console
function sendNotification(phoneNumber, message) {
	console.log('Sending notification to ' + phoneNumber + ', with message: ' + message);
}

const queueKey = 'push_notification_code';

queue.process(queueKey, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
});