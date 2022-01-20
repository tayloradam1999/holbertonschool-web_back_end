// Create array of jobObjs
const jobs = [
	{
	  phoneNumber: '4153518780',
	  message: 'This is the code 1234 to verify your account'
	},
	{
	  phoneNumber: '4153518781',
	  message: 'This is the code 4562 to verify your account'
	},
	{
	  phoneNumber: '4153518743',
	  message: 'This is the code 4321 to verify your account'
	},
	{
	  phoneNumber: '4153538781',
	  message: 'This is the code 4562 to verify your account'
	},
	{
	  phoneNumber: '4153118782',
	  message: 'This is the code 4321 to verify your account'
	},
	{
	  phoneNumber: '4153718781',
	  message: 'This is the code 4562 to verify your account'
	},
	{
	  phoneNumber: '4159518782',
	  message: 'This is the code 4321 to verify your account'
	},
	{
	  phoneNumber: '4158718781',
	  message: 'This is the code 4562 to verify your account'
	},
	{
	  phoneNumber: '4153818782',
	  message: 'This is the code 4321 to verify your account'
	},
	{
	  phoneNumber: '4154318781',
	  message: 'This is the code 4562 to verify your account'
	},
	{
	  phoneNumber: '4151218782',
	  message: 'This is the code 4321 to verify your account'
	}
  ];

// Create Kue queue
const kue = require('kue');
const queue = kue.createQueue();
const queueKey = 'push_notification_code_2';

// Iterate through each object in jobObjs array
jobs.forEach((jobObj) => {
	// create jobObj
	const job = queue.create(queueKey, jobObj).save((err) => {
		if (!err) console.log(`Notification job created: ${job.id}`);
	});

	// listen for jobObj completion
	job.on('complete', (result) => {
		console.log(`Notification job ${job.id} completed`);
	});

	// listen for jobObj failure
	job.on('failed', (errorMessage) => {
		console.log(`Notification job ${job.id} failed: ${errorMessage}`);
	});

	// listen for jobObj progress
	job.on('progress', (progress) => {
		console.log(`Notification job ${job.id} ${progress}% complete`);
	});
});
