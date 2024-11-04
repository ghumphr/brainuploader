# User Stories

## Content Creator
As a content creator, I want to generate new flashcard decks, so that I can organize study materials.

### Acceptance Criteria
- User needs to be able to create new flashcard decks
- User needs to be able to clone existing flashcard decks
- User needs to be able to combine existing flashcard decks
- User needs to be able to add flashcards to deck
- User needs to be able to delete flashcards from deck
- User needs to be able to edit flashcards in own decks
- User needs to be able to delete flashcard decks

## Student
As a student, I want to review information that I don't know yet so that I can learn it quickly.

### Acceptance Criteria
- User needs to be able to collect decks into stacks
- User needs to be able to review cards in stacks
- User needs search functionality
- User needs review mode that uses cards that meet query critera and disregards scheduling
- Scheduling algorithm must be implemented

## Instructor
As an instructor, I want to share specific flashcard decks with specific students or the public so they can learn the material.

### Acceptance Criteria
- User needs to be able to share decks with public
- User needs to be able to share decks with specific users

## AI Researcher
As an AI researcher, I want to extract all question/answer content in a simple and structured form so that I can inform language models.

### Acceptance Criteria
- User needs to be able to extract all card data programatically with a paged API call

## Critic
As a critic, I want others to see what I think about flashcards others have created.

### Acceptance Criteria

- User needs to be able to leave reviews on flashcards
- User needs to be able to leave reviews on decks
- User needs to be able to flag cards as incorrect
- User needs to be able to flag cards as possibly harmful 

# Misuser Stories

## Competitor
As a competitor, I want to steal all of the flashcards so I can use them in my own product.

### Mitigation Criteria
- All-card-access API must have authentication.
- Public APIs must use throttling
- Usage limits must be in place
- Administrator must be notified when usage limits are exceeded

## Disruptive User
As a disruptive user, I want to put obscene or harmful content into shared flashcards so that other users will be upset.

### Mitigation Criteria
- Administrator must have ability to warn/ban users
- Administrator must have ability to review user-flagged content
- Automated review should be performed to determine if content should be flagged offensive

## Mistaken/Incorrect User
As a mistaken user, I want to put incorrect answers on shared flashcards so that misinformation will spread.

### Mitigation Criteria
- Users should be notified if cards in decks or with identical content are flagged incorrect
- Scorecard for decks should be visible to all users who can see the deck
- Public scorecard should be kept for users


## Identity Thief
As an identity thief, I want to steal personal information from users on the website to use for fraudulent impersonation.

### Mitigation Criteria
- All passwords should be hashed
- Personal information like email addresses should not be displayed on user profiles
- System should be hardened against attacks

## Resource Hog
As a resource hog, I want to use large quantities of computing resources with no reasonable purpose.

### Mitigation Criteria
- One account per email address
- Limits on number of users created per day per IP address
- Limits on number of API calls per day per user
- Limits on number of cards that can be shared per day



