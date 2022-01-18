// Kue queueue
const kue = require('kue');
const queue = kue.createQueue();

// create data for job
const jobData = {
	phoneNumber: '4153518789',
	message: 'This is the code to verify your account',
};

// create job
const job = queue.create('push_notification_code', jobData).save(
	function(err) {
		if (err) {
			console.log(`Notification job failed`);
		}
		console.log(`Notification job created: ${job.id}`);
	},
	console.log(`Notification job completed`),
);
