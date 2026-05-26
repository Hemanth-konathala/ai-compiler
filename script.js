async function generateSystem() {

    const prompt =
        document
        .getElementById("prompt")
        .value
        .trim();

    const output =
        document
        .getElementById("output");

    if (!prompt) {

        output.textContent =
            "Please enter a prompt.";

        return;
    }

    output.textContent =
        "⚡ AI Compiler Running...";

    try {

        const response =
            await fetch(
                "https://ai-compiler-hawm.onrender.com",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        prompt: prompt
                    })
                }
            );

        const data =
            await response.json();

        output.textContent =
            JSON.stringify(
                data,
                null,
                4
            );

    }

    catch (error) {

        output.textContent =
            "Error: " +
            error.message;
    }
}