import createPushNotificationsJobs from "./8-job";
import { createQueue } from "kue";
import { expect } from "chai";

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    // enter test mode before test starts
    queue.testMode.enter();
  });

  afterEach(() => {
    // clear queue after each test
    queue.testMode.clear();
  });

  after(() => {
    // exit test mode after all tests
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not a valid array', queue))
      .to.throw('Jobs is not an array');
  });

  it('should create 2 new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Testing message for phone 1' },
      { phoneNumber: '0987654321', message: 'Testing message for phone 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should not create jobs if array is empty', () => {
    createPushNotificationsJobs([], queue)
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('should throw an error if null is passed as input', () => {
    expect(() => createPushNotificationsJobs(null, queue))
      .to.throw('Jobs is not an array');
  });

  it('should throw an error if undefined is passed as input', () => {
    expect(() => createPushNotificationsJobs(undefined, queue))
      .to.throw('Jobs is not an array');
  });
});
