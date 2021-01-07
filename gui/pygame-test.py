import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球')
  
  screen.fill((242, 242, 242))
  # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
  pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
  # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
  pygame.display.flip()
  
  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == '__main__':
  main()