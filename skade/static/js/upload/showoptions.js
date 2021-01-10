function toggleOptions() {
    config_options = document.getElementById('options')
    if (config_options.classList.contains('is-hidden')) {
        config_options.classList.remove('is-hidden')
    } else {
        config_options.classList.add('is-hidden')
    }
}