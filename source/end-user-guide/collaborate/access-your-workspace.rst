Access your workspace
=====================

You can access Mattermost with your credentials using a web browser, the desktop app, or the mobile app. You will log in with your email, username, or Single Sign-On (SSO), depending on how your system admin has configured it.

.. tip::

  **Can't find your Mattermost link?** Ask your company's IT department or your system admin for the **Mattermost Site URL**. It will look something like ``https://example.com/company/mattermost`` or ``chat.yourcompanydomain.com``.

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

  Install the desktop app </end-user-guide/collaborate/install-desktop-app>
  Install the iOS mobile app </end-user-guide/collaborate/install-ios-app>
  Install the Android mobile app </end-user-guide/collaborate/install-android-app>
  Log out of Mattermost </end-user-guide/collaborate/log-out>

.. tab:: Web/Desktop
  :parse-titles:

  Web browser
  -----------

  1. Open a supported :ref:`web browser <deployment-guide/software-hardware-requirements:pc web>`.
  2. Copy and paste the Mattermost server link into the browser's address field.
  3. Enter your credentials to log in.
  4. Bookmark the Mattermost URL for easy future access.

  Desktop app
  -----------------

  1. Download and install the Mattermost desktop app (from the App Store for macOS, Microsoft Store for Windows, or :doc:`using a package manager for Linux </deployment-guide/desktop/linux-desktop-install>`).
  2. Enter the Mattermost server link and a display name for the instance. The display name is helpful if you connect to multiple servers.
  3. Enter your credentials to log in.
  4. The first team in the team sidebar opens. If you are not a member of a team, you will be prompted to join one.

  .. note::

    When you log in with external credentials (like Google or Entra ID), the desktop app will temporarily close for authentication. Once logged in, you will be returned to the app.

.. tab:: Mobile
  :parse-titles:

  1. Download and install the Mattermost mobile app from the `Apple App Store (iOS) <https://www.apple.com/app-store/>`__ or `Google Play Store (Android) <https://play.google.com/store/games?hl=en>`__.
  2. Enter the Mattermost server link (must begin with ``http://`` or ``https://``) and a display name for the instance.
  3. Enter your credentials to log in.
  4. The first team in the team sidebar opens. If you are not a member of a team, you will be prompted to join one.

Login Options
--------------------

Depending on your admin's settings, you can use the following options to log in.

Email address or username
~~~~~~~~~~~~~~~~~~~~~~~~

When :ref:`account creation with email <administration-guide/configure/authentication-configuration-settings:enable account creation with email>` is enabled, you can log in with the email or username you used to create the account.

.. image:: ../../images/login-email-username.png
  :alt: Log in to Mattermost with your username or email address, or reset your password.

Single Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~

If enabled by your system admin, you can log in with your GitLab, Google, Ent