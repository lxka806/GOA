# Todo App

The app uses Django's built-in user authentication with cookie-based sessions.
Each signed-in user can only see and manage their own tasks.

## Run locally

1. In `backend`, run `python manage.py migrate` and then `python manage.py runserver`.
2. In `frontend`, run `npm install` and `npm run dev`.
3. Open the Vite URL (localhost or 127.0.0.1) and register an account.

The frontend requests a CSRF cookie before login or registration. Keep the
frontend and backend on the same hostname (`localhost` or `127.0.0.1`) so the
browser can send the session cookie.

## Frontend tooling

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.
