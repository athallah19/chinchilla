const setCaret = (el) => {
    if (!el) return;

    try {
        const range = document.createRange();
        const sel = window.getSelection();

        range.setStart(el.childNodes[0], el.innerText.length);
        range.collapse(true);

        sel.removeAllRanges();
        sel.addRange(range);
    } catch (err) {
        console.log("Error Setting Caret: ", err);
    }
};

const togglePassword = (button) => {
    button.classList.toggle("showing");
    const input = document.getElementById("password");
    input.type = input.type === "password" ? "text" : "password";
    input.focus();
    setCaret(input);
};

document.getElementById('kembali').addEventListener('click', function () {
    window.history.back();
});



function login() {
    let username = $("#input-username").val();
    let password = $("#password").val();
    if (!username || !password) {
        alert("Mohon lengkapi username dan password.");
        return;
    }

    $.ajax({
        type: "POST",
        url: "/login_save",
        data: {
            username_login: username,
            password_login: password,
        },
        success: function (response) {
            if (response["result"] === "success") {
                let token = response["token"];
                $.cookie("mytoken", token, { path: "/" });
                alert("Login Berhasil!");
                window.location.href = "/dashboard";
            } else {
                alert(response["msg"]);
            }
        },
    });
}

function log_out() {
    $.removeCookie("mytoken", { path: "/" });
    alert("Anda telah keluar");
    window.location.href = "/login";
}