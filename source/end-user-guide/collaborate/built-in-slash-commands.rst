Use built-in slash commands
============================

.. include:: ../../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can interact with Mattermost users, channels, and conversations using slash commands directly in the message box.

.. tip::

    Looking for more slash commands? See the `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`__ developer documentation for details on creating custom commands.

Commands for channels and invites
---------------------------------

These commands help you manage channels and invite people to your workspace.

* **Invite people:**
    - To invite one person: ``/invite @username`` (e.g., ``/invite @alice``)
    - To invite a user group: ``/invite @usergroup``
    - To invite multiple people to a channel: ``/invite @user1 @user2 ~channel-name`` (e.g., ``/invite @bob @sally ~project-alpha``)
    
* **Manage channels:**
    - To join a channel: ``/join {channel-name}`` (e.g., ``/join marketing-team``)
    - To leave a channel: ``/leave``
    - To mute a channel (turn off notifications): ``/mute {channel-name}`` (e.g., ``/mute announcements``)
    - To remove someone from a channel: ``/kick {@username}`` (e.g., ``/kick @john``)

Commands for conversations
--------------------------

These commands are useful for managing your conversations and messages.

* **Send a direct message:**
    - To send a direct message to a person: ``/msg {@username} {message}`` (e.g., ``/msg @maria What's the latest?``)
    
* **Format messages:**
    - To display text as a code block: ``/code {text}``
    - To respond with a shrug: ``/shrug {message}`` (e.g., ``/shrug I don't know the answer``)

Commands for status
--------------------

These commands change your status and availability in Mattermost.

* **Change availability:**
    - To set your status to away: ``/away``
    - To set your status to offline: ``/offline``
    - To set your status to available: ``/online``
    - To set your status to Do Not Disturb: ``/dnd``
    
* **Set a custom status:**
    - To set a custom status with an emoji: ``/status {emoji_name} {message}`` (e.g., ``/status coffee In a meeting``)
    - To clear your custom status: ``/status clear``