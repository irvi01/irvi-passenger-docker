module.exports = [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        document: "readonly",
        window: "readonly",
        fetch: "readonly",
        alert: "readonly",
        localStorage: "readonly",
        atob: "readonly",
      },
    },
    rules: {
      "no-unused-vars": "off",
      "no-console": "warn",
      "no-undef": "error",
      "semi": ["error", "always"],
      "quotes": ["error", "double"],
    },
  },
];
