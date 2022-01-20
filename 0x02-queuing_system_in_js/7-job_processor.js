const kue = require('kue');

// add blacklisted numbers in array
const blacklist = [
	'4153518780',
	'4153518781',
];

function sendNotification(phoneNumber, message, job, done) {
	// on function call, track progress of <job> 0 out of 100
	job.progress(0, 100);
	// check for blacklisted number
	if (blacklist.includes(phoneNumber)) {
		// if blacklisted, throw error
		done(Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}
	// track progress of <job> 50 out of 100
	job.progress(50, 100);
	// log notification
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
	// use done argument to indicate success
	done();
}

// create kue queue that will proceed job of the queue 'push_notification_code_2'
// with two jobs at the same time
const queue = kue.createQueue();
const queueKey = 'push_notification_code_2';

// process two jobs at the same time
queue.process(queueKey, 2, (job, done) => {
	// call function sendNotification with job data
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
