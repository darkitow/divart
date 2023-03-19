from PIL import Image

# 2048 / 1024
IMAGE_SIZE = 2048, 1024
BACKGROUND_SIZE = 1280, 720
COVER_SIZE = 510, 510

image = Image.new( "RGBA", IMAGE_SIZE, "#00000000" )

background = Image.open( "bg.png" ).resize( BACKGROUND_SIZE )
cover = Image.open( "cover.png" ).resize( COVER_SIZE )

image.paste( background, (0,0) )
image.paste( cover, (1280,0) )

image.save("out.png")