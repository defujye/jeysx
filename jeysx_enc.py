#FACEBOOK : https://facebook.com/ujfye
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))