#=========== Design an Email Simulator ==============#
# Description: A simple Email Simulator that allows users to send, receive, read, list, and delete emails.


'''
# Define Requirements / Scope
Functional Requirements
- User should be able to send an email to another user.
- Each user should have an inbox.
- Inbox should support:
    - Listing all emails
    - Reading a specific email
    - Deleting an email
- Email should contain:
    - Sender
    - Receiver
    - Subject
    - Body
    - Timestamp
    - Read/Unread status

Non-Functional Requirements
- Simple, in-memory storage (no database)
- Object-oriented design
- Easy to extend (attachments, CC, search, etc.)


# Core Entities:
1. User	    Represents a user who can send and receive emails
2. Email	Represents an email message
3. Inbox	Stores and manages emails for a user
'''

#==================== Create Classes and Define Methods ===================#

# Store/Refer time wherever needed
import datetime

class Email:
    # Represents a single email message.
    def __init__(self, sender, receiver, subject, body):
        # User who sends the email
        self.sender = sender
        # User who receives the email
        self.receiver = receiver
        # Subject line of the email
        self.subject = subject
        # Main email content
        self.body = body
        # Timestamp when the email is created
        self.timestamp = datetime.datetime.now()
        # Read status (False = Unread, True = Read)
        self.read = False

    # Marks the email as read.
    def mark_as_read(self):
        self.read = True

    # Displays full details of the email and marks it as read.
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # String representation of the email for inbox listing.
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    

class Inbox:
    # Represents a user's inbox.
    def __init__(self):
        # Stores all received emails
        self.emails = []

    # Adds a new email to the inbox.
    def receive_email(self, email):
        self.emails.append(email)

    # Displays a summary of all emails in the inbox.
    def list_emails(self):
        # Check for emails first
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        # Fix the indexing as defaut starts from 0
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Reads an email based on its index.
    def read_email(self, index):
        # Check for emails first
        if not self.emails:
            print('Inbox is empty.\n')
            return
        # Fix the indexing
        actual_index = index - 1
        # Check for outliers / limits
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # Display the contents of the email
        self.emails[actual_index].display_full_email()

    # Deletes an email from the inbox.
    def delete_email(self, index):
        # Check for emails first
        if not self.emails:
            print('Inbox is empty.\n')
            return
        # Fix the indexing
        actual_index = index - 1
        # Check for outliers / limits
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # Delete the fetched email wrt index
        del self.emails[actual_index]
        print('Email deleted.\n')


class User:
    # Represents a user in the email system.
    def __init__(self, name):
        self.name = name
        # Each user has their own inbox
        self.inbox = Inbox()

    # Sends an email to another user.
    def send_email(self, receiver, subject, body):
        # Define object for email with updated parameters
        email = Email( sender=self, receiver=receiver, subject=subject, body=body)
        # Add email to receiver's inbox
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Lists all emails in the user's inbox.
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # Reads a specific email.
    def read_email(self, index):
        self.inbox.read_email(index)

    # Deletes a specific email.
    def delete_email(self, index):
        self.inbox.delete_email(index)



# Calling objects and verifying functions
def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    # Test case
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()

if __name__ == '__main__':
    main()