// test file for 8-job.js
const kue = require('kue');
const queue = kue.createQueue();
const chai = require('chai');
const expect = chai.expect;
const createPushNotificationsJobs = require('./8-job');

describe("createPushNotificationsJobs", () => {
	it("check error thrown from job array being Number", () => {
		expect(() => {
			createPushNotificationsJobs(1, queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check error thrown from job array being String", () => {
		expect(() => {
			createPushNotificationsJobs("string", queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check error thrown from job array being Object", () => {
		expect(() => {
			createPushNotificationsJobs({}, queue);
		}).to.throw(Error, 'Jobs is not an array');
	});

	it("check what is thrown if job is array", () => {
		expect(() => {
			createPushNotificationsJobs([], queue);
		}).to.not.throw(Error, 'Jobs is not an array');
	});
})