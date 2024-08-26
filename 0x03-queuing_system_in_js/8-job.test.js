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
});
