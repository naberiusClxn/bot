# Project: Discord Bot for Automated Messages

## Project Goals

1. **Simplify Communication**: Create a convenient and functional way to manage voice sessions, events, and posters via commands.
2. **Effective Role Management**: Ensure that only users with specific roles have access to the functionality.
3. **User Support**: Provide simple and understandable commands for interacting with the bot.

---

## Testing Scenarios

### General Requirements

- Ensure the bot is running and accessible on the Discord server.
- The user must have a role specified in `ROLE_PERMISSIONS`.
- All commands are tested using slash commands.

---

### Testing the `/voice` Command

**Description**: Creates a message about a scheduled voice-over session.

1. **Steps**:
   - Enter the `/voice` command.
   - Provide the parameters:
     - `title`: The anime title.
     - `description`: A brief description of the voice-over.
     - `voice_link`: A link to the voice channel.
     - `hosts`: The voice-over hosts.
     - `photo_url`: A link to an image (optional).
   - Send the command.

2. **Expected Result**:
   - The bot sends an embed message with the provided information.
   - If the user lacks permissions, the bot responds: "You do not have permission to execute this command."

---

### Testing the `/creativity` Command

**Description**: Creates a message about a creative event.

1. **Steps**:
   - Enter the `/creativity` command.
   - Provide the parameters:
     - `title`: The title of the creative event.
     - `description`: A brief description of the event.
     - `event_url`: A link to the event.
     - `photo_url`: A link to an image (optional).
   - Send the command.

2. **Expected Result**:
   - The bot sends an embed message with the provided information.
   - If the user lacks permissions, the bot responds: "You do not have permission to execute this command."

---

### Testing the `/poster` Command

**Description**: Creates a message about an event poster.

1. **Steps**:
   - Enter the `/poster` command.
   - Provide the parameters:
     - `title`: The title of the poster.
     - `duration`: The event duration.
     - `genre`: The event genre.
     - `age`: The age restrictions.
     - `description`: A brief description of the event.
     - `event_url`: A link to the event.
     - `photo_url`: A link to an image.
   - Send the command.

2. **Expected Result**:
   - The bot sends an embed message with the provided information.
   - If the user lacks permissions, the bot responds: "You do not have permission to execute this command."

---

### Additional Checks

1. **Role Validation**:
   - Attempt to execute commands with an account that does not have the required role.
   - Verify that the bot correctly denies access with an appropriate message.

2. **Data Validation**:
   - Test commands with incorrect or empty parameter values.

3. **Visual Test**:
   - Verify how embed messages are displayed on Discord for both desktop and mobile devices.

---



