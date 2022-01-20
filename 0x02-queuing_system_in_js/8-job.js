const kue = require('kue');


const createPushNotificationsJobs = (jobs, queue) => {
	// check if jobs is an array
	if (!Array.isArray(jobs)) {
		throw new Error(`Jobs is not an array`);
	}
	// Iterate through each object in jobs array and create job in queue
	jobs.forEach((jobObj) => {
		// create job
		const job = queue.create('push_notification_code_3', jobObj).save((err) => {
			if (!err) console.log(`Notification job created: ${job.id}`);
		});
		
		// listen for job completion
		job.on('complete', () => {
			console.log(`Notification job ${job.id} completed`);
		});

		// listen for job error
		job.on('failed', (err) => {
			console.log(`Notification job ${job.id} failed: ${err}`);
		});

		// listen for job progress
		job.on('progress', (progress) => {
			console.log(`Notification job ${job.id} ${progress}% complete`);
	});
	});
}

module.exports = createPushNotificationsJobs;