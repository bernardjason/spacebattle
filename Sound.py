try:

    import simpleaudio as sa

    player_fire = sa.WaveObject.from_wave_file('fire.wav')
    asteroid_explode = sa.WaveObject.from_wave_file('explode.wav')
    player_hit = sa.WaveObject.from_wave_file('dead.wav')


    def fire():
        global player_fire
        player_fire.play()

    def player_dead():
        global player_hit
        player_hit.play()

    def explode():
        global asteroid_explode
        asteroid_explode.play()

except ImportError as e:

    def fire():
        return

    def player_dead():
        return

    def explode():
        return
