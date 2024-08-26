import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.log('Notification job failed');
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
