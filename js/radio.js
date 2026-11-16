// User-initiated playback of the same HTTPS relay used by Moonpet.
document.querySelectorAll('.radio-panel').forEach(panel => {
  const audio = panel.querySelector('audio');
  const status = panel.querySelector('.radio-status');
  const retry = panel.querySelector('.radio-retry');
  function message(text) { status.textContent = text; }
  audio.volume = 0.5;
  audio.addEventListener('loadstart', () => message('Connecting to GraffPUNKS Radio…'));
  audio.addEventListener('playing', () => { retry.hidden = true; message('Playing GraffPUNKS Radio.'); });
  audio.addEventListener('pause', () => { if (!audio.error) message('Radio paused.'); });
  audio.addEventListener('waiting', () => message('Buffering the live stream…'));
  audio.addEventListener('error', () => {
    retry.hidden = false;
    message('Radio unavailable. Retry, or open the stream separately.');
  });
  retry.addEventListener('click', () => {
    retry.hidden = true;
    audio.load();
    audio.play().catch(() => {
      retry.hidden = false;
      message('Playback could not start. Press play or retry.');
    });
  });
  window.addEventListener('pagehide', () => {
    audio.pause();
    audio.removeAttribute('src');
    audio.load();
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted) {
      audio.src = 'https://api.cryptomoonboys.com/radio/stream';
      message('Press play to listen.');
    }
  });
});
