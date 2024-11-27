from flask import Flask, render_template, request, jsonify
import pygame
import os

app = Flask(__name__)


def run_hologram_code(video_path):

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hologram")
    if not os.path.exists(video_path):
        return "Video file not found."
    from moviepy.editor import VideoFileClip

    clip = VideoFileClip(video_path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()
    return "Hologram displayed successfully!"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run_hologram', methods=['POST'])
def run_hologram():
    video_path = 'Hologram.mp4'
    hologram_result = run_hologram_code(video_path)
    return jsonify({"result": hologram_result})


if __name__ == '__main__':
    app.run(debug=True)
