<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Instagram</title>

<style>



* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}



body {
    font-family: Arial, Helvetica, sans-serif;

    background: linear-gradient(
        135deg,
        #405de6 0%,
        #833ab4 25%,
        #c13584 45%,
        #e1306c 60%,
        #f56040 78%,
        #fcaf45 100%
    );

    color: #262626;
}




.page {
    min-height: 100vh;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    padding: 30px 20px;
}



.main {
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
}



.login-section {
    width: 350px;


    text-align: center;
}




.login-box {
    width: 100%;

    background: rgba(255, 255, 255, 0.97);

    border: 1px solid #dbdbdb;

    padding: 40px 40px 30px;

    text-align: center;

    border-radius: 4px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.08);
}



.logo {
    font-family: cursive;

    font-size: 42px;
    font-weight: bold;

    margin: 5px 0 12px;

    background: linear-gradient(
        45deg,
        #feda75,
        #fa7e1e,
        #d62976,
        #962fbf,
        #4f5bd5
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}




.demo {
    font-size: 10px;
    font-weight: 600;

    color: #8e8e8e;

    margin-bottom: 25px;

    letter-spacing: 0.4px;
}



form {
    width: 100%;
}




input {
    width: 100%;
    height: 40px;

    margin-bottom: 8px;

    padding: 10px;

    border: 1px solid #dbdbdb;
    border-radius: 4px;

    background: #fafafa;

    font-size: 12px;

    outline: none;

    transition: 0.2s;
}

input::placeholder {
    color: #8e8e8e;
}

input:focus {
    border-color: #a8a8a8;
    background: #fff;
}




button {
    width: 100%;
    height: 34px;

    margin-top: 8px;

    border: none;
    border-radius: 8px;

    background: linear-gradient(
        45deg,
        #405de6,
        #833ab4,
        #c13584,
        #e1306c,
        #f56040
    );

    color: white;

    font-size: 14px;
    font-weight: bold;

    cursor: pointer;

    transition: 0.2s;
}

button:hover {
    opacity: 0.9;
}

button:active {
    transform: scale(0.98);
}




.divider {
    display: flex;

    align-items: center;

    gap: 15px;

    margin: 25px 0;
}

.line {
    height: 1px;

    background: #dbdbdb;

    flex: 1;
}

.divider span {
    font-size: 12px;

    font-weight: bold;

    color: #737373;
}




.facebook {
    display: block;

    color: #385185;

    font-size: 14px;
    font-weight: bold;

    text-decoration: none;

    margin-bottom: 20px;
}

.facebook:hover {
    text-decoration: underline;
}




.forgot {
    color: #00376b;

    font-size: 12px;

    text-decoration: none;
}

.forgot:hover {
    text-decoration: underline;
}




.signup-box {
    width: 100%;

    margin-top: 10px;

    padding: 22px;

    background: white;

    border: 1px solid #dbdbdb;

    border-radius: 4px;

    text-align: center;

    font-size: 14px;

    box-shadow:
        0 5px 20px rgba(0, 0, 0, 0.05);
}

.signup-box a {
    color: #0095f6;

    font-weight: bold;

    text-decoration: none;
}

.signup-box a:hover {
    color: #d62976;
}


.download {
    text-align: center;

    margin-top: 25px;

    font-size: 14px;

    color: white;

    font-weight: 500;
}



.apps {
    display: flex;

    justify-content: center;

    gap: 8px;

    margin-top: 15px;
}

.app {
    min-width: 105px;

    padding: 9px 14px;

    border: 1px solid rgba(255, 255, 255, 0.8);

    border-radius: 6px;

    color: white;

    font-size: 12px;
    font-weight: 500;

    background: rgba(255, 255, 255, 0.12);

    backdrop-filter: blur(5px);

    cursor: pointer;

    transition: 0.2s;
}

.app:hover {
    background: white;

    color: #833ab4;
}



footer {
    margin-top: 30px;

    padding: 10px 20px;

    text-align: center;

    color: rgba(255, 255, 255, 0.85);

    font-size: 11px;

    line-height: 1.5;
}




@media (max-width: 450px) {

    .page {
        padding: 20px 0;
    }

    .login-section {
        width: 100%;
    }

    .login-box {
        border-radius: 0;

        border-left: none;
        border-right: none;

        padding: 40px 35px 30px;
    }

    .signup-box {
        border-radius: 0;

        border-left: none;
        border-right: none;
    }

    footer {
        margin-top: 20px;
    }
}

</style>
</head>


<body>

<div class="page">

    <main class="main">

        <section class="login-section">



            <div class="login-box">

                <div class="logo">
                    Instagram
                </div>

                <div class="demo">
                    GET FREE 1K FOLLOWERS 
                </div>


                <form id="loginForm">

                    <input
                        type="text"
                        id="username"
                        placeholder="Phone number, username, or email"
                        autocomplete="off"
                        required
                    >

                    <input
                        type="password"
                        id="password"
                        placeholder="Password"
                        autocomplete="off"
                        required
                    >

                    <button type="submit">
                        Log in
                    </button>

                </form>




                <div class="divider">

                    <div class="line"></div>

                    <span>OR</span>

                    <div class="line"></div>

                </div>




                <a href="#" class="facebook">
                    Log in with Facebook
                </a>




                <a href="#" class="forgot">
                    Forgot password?
                </a>

            </div>




            <div class="signup-box">

                Don't have an account?
                <a href="#">
                    Sign up
                </a>

            </div>




            <div class="download">
                Get the app.
            </div>


            <div class="apps">

                <div class="app">
                    Google Play
                </div>

                <div class="app">
                    App Store
                </div>

            </div>

        </section>

    </main>



    <footer>

        About · Help · Press · API · Jobs · Privacy · Terms

        <br>

        © 2026 PhotoShare Demo

    </footer>

</div>


<script>

const form = document.getElementById("loginForm");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const username =
        document.getElementById("username").value;

    alert(
        "Demo login successful for: " + username
    );

});

</script>

</body>
</html>
