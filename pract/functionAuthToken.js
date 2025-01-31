// Create a function that returns tokens

// Rewrite createAuthService to include a resetToken method that sets token to an empty string.

function createAuthService() {
    let token = ""; // Private variable

    return {
        setToken: (userToken) => (token = userToken), // Updates private token to user's token
        getToken: () => token,
        resetToken: () => (token = "")
}

}
const authService = createAuthService()

authService.setToken("abc123")
console.log(authService.getToken())

authService.resetToken()
console.log(authService.getToken())

