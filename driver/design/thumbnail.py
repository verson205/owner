import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"https://telegra.ph/file/a2b3e05ff5b0f32fe389b.jpg", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"https://telegra.ph/file/a2b3e05ff5b0f32fe389b.jpg")
    image2 = Image.open("driver/source/LightBlue.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"https://telegra.ph/file/a2b3e05ff5b0f32fe389b.jpg")
    img = Image.open(f"https://telegra.ph/file/a2b3e05ff5b0f32fe389b.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("driver/source/regular.ttf", 52)
    font2 = ImageFont.truetype("driver/source/medium.ttf", 76)
    draw.text(
        (25, 610),
        f"{title[:18]}...",
        fill="black",
        font=font2,
    )
    draw.text(
        (27, 535),
        f"??????? ??? ?????? {ctitle[:8]}...",
        fill="red",
        font=font,
    )
    img.save(f"https://telegra.ph/file/a2b3e05ff5b0f32fe389b.jpg")
    os.remove(f"search/temp{userid}.png")
    os.remove(f"search/thumb{userid}.png")
    final = f"search/final{userid}.png"
    return final
