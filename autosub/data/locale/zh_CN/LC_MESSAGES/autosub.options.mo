��    I      d  a   �      0     1  h   Q  p   �  g   +  �   �  �     |    	  }   }	    �	     �
       D   '  �  l  4  8  n   m  A   �      �   ;     �  =   �    8  ]   :  �   �     3     D  �   Q       �     �    ;  �  z     J   �  J   �        Z   0  ]   �    �  J      $   K     p     �     �     �  `   �  7   ?     w     �     �  �  �  �   �  j   [   S   �   �   !  !   �!  !   �!  5  "  2   J#  -   }#     �#     �#  �   �#  �   �$  q   {%  �   �%  �   �&  �  ='  O  �)    >+  |  Q,  �   �-     �.     �.  ;  �.  '   �/  �   0  �   �0  q   *1  �   �1  �   h2  �   �2  �   �3  =  24     p5     �5  F   �5     �5  V  �7  d   39  F   �9  T  �9  �   4;     �;  O   �;    E<  s   `=  �   �=     �>     �>  �   �>     y?    �?  I  �@  H  �B  �   CD  o   �D  o   _E     �E  b   �E  f   ?F  K  �F  F   �H     9I     XI     qI     �I     �I  !   �I     �I     �I     
J     )J  `  6J  �   �L  p   lM  _   �M  �   =N  +   �N  .   �N  .  $O  ?   SP  ?   �P     �P     �P  �   �P  �   �Q  w   �R  �   4S  �   �S  �  }T  Y  UW  >  �X  �  �Y  �   �[     �\     �\     -   7         C                             =   &   ?   A   $      @   1       "   6   '   (   ,   2            9   F       .          !          B                 E         %   D           0       I       :   3   
   4         H   *   <      /      8   +          >               G   )       5                                    	      ;      #            
  %(prog)s [-i path] [options] (Experimental)This arg will override the default API audio channel. (arg_num = 1) (default: %(default)s) (Experimental)This arg will override the default API audio sample rate(Hz). (arg_num = 1) (default: %(default)s) (Experimental)This arg will override the default API audio suffix. (arg_num = 1) (default: %(default)s) (Experimental)This arg will override the default audio conversion command. "[", "]" are optional arguments meaning you can remove them. "{", "}" are required arguments meaning you can't remove them. (arg_num = 1) (default: %(default)s) (Experimental)This arg will override the default audio split command. Same attention above. (arg_num = 1) (default: %(default)s) Add http proxy by setting environment variables. If arg_num is 0, use const proxy url. (arg_num = 0 or 1) (const: %(const)s) Add https proxy by setting environment variables. If arg_num is 0, use const proxy url. (arg_num = 0 or 1) (const: %(const)s) An integer between 0 and 100 to control the good match group of "-lsc"/"--list-speech-codes" or "-ltc"/"--list-translation-codes" or the match result in "-bm"/"--best-match". Result will be a group of "good match" whose score is above this arg. (arg_num = 1) Audio Processing Options Auditok Options Change the Google Speech V2 API URL into the http one. (arg_num = 0) Choose which Speech-to-Text API to use. Currently support: gsv2: Google Speech V2 (https://github.com/gillesdemey/google-speech-v2). gcsv1: Google Cloud Speech-to-Text V1P1Beta1 (https://cloud.google.com/speech-to-text/docs). xfyun: Xun Fei Yun Speech-to-Text WebSocket API (https://www.xfyun.cn/doc/asr/voicedictation/API.html). baidu: Baidu Automatic Speech Recognition API (https://ai.baidu.com/ai-doc/SPEECH/Vk38lxily) (arg_num = 1) (default: %(default)s) Destination subtitles format. If not provided, use the extension in the "-o"/"--output" arg. If "-o"/"--output" arg doesn't provide the extension name, use "{dft}" instead. In this case, if "-i"/"--input" arg is a subtitles file, use the same extension from the subtitles file. (arg_num = 1) (default: {dft}) Drop any .ass override codes in the text before translation. Only affect the translation result. (arg_num = 0) Drop any regions without speech recognition result. (arg_num = 0) Google Speech-to-Text API response for text confidence. A float value between 0 and 1. Confidence bigger means the result is better. Input this argument will drop any result below it. Ref: https://github.com/BingLingGroup/google-speech-v2#response (arg_num = 1) (default: %(default)s) If not input this option, it will keep all regions strictly follow the minimum region limit. Ref: https://auditok.readthedocs.io/en/latest/core.html#class-summary (arg_num = 0) Input Options Keep audio processing files to the output path. (arg_num = 0) Lang code/Lang tag for speech-to-text. Recommend using the Google Cloud Speech reference lang codes. WRONG INPUT WON'T STOP RUNNING. But use it at your own risk. Ref: https://cloud.google.com/speech-to-text/docs/languages(arg_num = 1) (default: %(default)s) Lang code/Lang tag for translation destination language. (arg_num = 1) (default: %(default)s) Lang code/Lang tag for translation source language. If not given, use py-googletrans to auto-detect the src language. (arg_num = 1) (default: %(default)s) Language Options List Options List all available "-SRC"/"--src-language" py-googletrans translation language codes. Or else will list a group of "good match" of the arg. Same docs above. (arg_num = 0 or 1) List all available arguments. List all available subtitles formats. If your format is not supported, you can use ffmpeg or SubtitleEdit to convert the formats. You need to offer fps option when input is an audio file and output is "sub" format. (arg_num = 0) List all recommended "-S"/"--speech-language" Google Speech-to-Text language codes. If no arg is given, list all. Or else will list a group of "good match" of the arg. Default "good match" standard is whose match score above 90 (score between 0 and 100). Ref: https://tools.ietf.org/html/bcp47 https://github.com/LuminosoInsight/langcodes/blob/master/langcodes/__init__.py lang code example: language-script-region-variant-extension-privateuse (arg_num = 0 or 1) Make sure the argument with space is in quotes.
The default value is used
when the option is not given at the command line.
"(arg_num)" means if the option is given,
the number of the arguments is required.
Arguments *ARE* the things given behind the options.
Author: {author}
Email: {email}
Bug report: {homepage}
 Maximum length of a tolerated silence within a valid audio activity. Same docs above. (arg_num = 1) (default: %(default)s) Maximum region size. Same docs above. (arg_num = 1) (default: %(default)s) Minimum region size. Same docs above. (arg_num = 1) (default: %(default)s) Network Options Number of concurrent Speech-to-Text requests to make. (arg_num = 1) (default: %(default)s) Number of concurrent ffmpeg audio split process to make. (arg_num = 1) (default: %(default)s) Option to control audio process. If not given the option, do normal conversion work. "y": pre-process the input first then start normal workflow. If succeed, no more conversion before the speech-to-text procedure. "o": only pre-process the input audio. ("-k"/"--keep" is true) "s": only split the input audio. ("-k"/"--keep" is true) Default command to pre-process the audio: {dft_1} | {dft_2} | {dft_3} (Ref: https://github.com/stevenj/autosub/blob/master/scripts/subgen.sh https://ffmpeg.org/ffmpeg-filters.html) (2 >= arg_num >= 1) Options to control Auditok when not using external speech regions control. Options to control audio processing. Options to control input. Options to control language. Options to control network. Options to control output. Options to control speech-to-text. If Speech Options not given, it will only generate the times. Options to control subtitles conversions.(Experimental) Other Options Other options to control. Output Options Output more files. Available types: regions, src, full-src, dst, bilingual, dst-lf-src, src-lf-dst, all. "regions", "src", "full-src" are available only if input is not a subtitles file. full-src: Full result received from Speech-to-Text API in json format with start and end time. dst-lf-src: dst language and src language in the same event. And dst is ahead of src. src-lf-dst: src language and dst language in the same event. And src is ahead of dst. (6 >= arg_num >= 1) (default: %(default)s) Path to the subtitles file which provides external speech regions, which is one of the formats that pysubs2 supports and overrides the default method to find speech regions. (arg_num = 1) Prevent pauses and allow files to be overwritten. Stop the program when your args are wrong. (arg_num = 0) Ref: https://auditok.readthedocs.io/en/latest/core.html#class-summary (arg_num = 0) Replace the specific chars with a space after translation, and strip the space at the end of each sentence. Only affect the translation result. (arg_num = 0 or 1) (const: %(const)s) Set proxy password. (arg_num = 1) Set proxy username. (arg_num = 1) Set service account key environment variable. It should be the file path of the JSON file that contains your service account credentials. Can be overridden by the API key. Ref: https://cloud.google.com/docs/authentication/getting-started Currently support: gcsv1 (GOOGLE_APPLICATION_CREDENTIALS) (arg_num = 1) Show %(prog)s help message and exit. (arg_num = 0) Show %(prog)s version and exit. (arg_num = 0) Speech Options Subtitles Conversion Options The API key for Google Speech-to-Text API. (arg_num = 1) Currently support: gsv2: The API key for gsv2. (default: Free API key) gcsv1: The API key for gcsv1. (If used, override the credentials given by"-sa"/"--service-account") The energy level which determines the region to be detected. Ref: https://auditok.readthedocs.io/en/latest/apitutorial.html#examples-using-real-audio-data (arg_num = 1) (default: %(default)s) The output path for subtitles file. (default: the "input" path combined with the proper name tails) (arg_num = 1) The path to the video/audio/subtitles file that needs to generate subtitles. When it is a subtitles file, the program will only translate it. (arg_num = 1) This arg will override the default audio pre-process command. Every line of the commands need to be in quotes. Input file name is {in_}. Output file name is {out_}. (arg_num >= 1) Use Speech-to-Text recognition config file to send request. Override these options below: "-S", "-asr", "-asf". Currently support: gcsv1: Google Cloud Speech-to-Text V1P1Beta1 API key config reference: https://cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig Service account config reference: https://googleapis.dev/python/speech/latest/gapic/v1/types.html#google.cloud.speech_v1.types.RecognitionConfig xfyun: Xun Fei Yun Speech-to-Text WebSocket API (https://console.xfyun.cn/services/iat). baidu: Baidu Automatic Speech Recognition API (https://ai.baidu.com/ai-doc/SPEECH/ek38lxj1u). If arg_num is 0, use const path. (arg_num = 0 or 1) (const: %(const)s) Use langcodes to get a best matching lang code when your input is wrong. Only functional for py-googletrans and Google Speech API. If langcodes not installed, use fuzzywuzzy instead. Available modes: s, src, d, all. "s" for "-S"/"--speech-language". "src" for "-SRC"/"--src-language". "d" for "-D"/"--dst-language". (3 >= arg_num >= 1) Use py-googletrans to detect a sub file's first line language. And list a group of matched language in recommended "-S"/"--speech-language" Google Speech-to-Text language codes. Ref: https://cloud.google.com/speech-to-text/docs/languages (arg_num = 1) (default: %(default)s) Valid when your output format is "ass"/"ssa" and "-sty"/"--styles" is given. Adds "ass"/"ssa" styles to your events. If not provided, events will use the first one from the file. If the arg_num is 1, events will use the specific style from the arg of "-sty"/"--styles". If the arg_num is 2, src language events use the first. Dst language events use the second. (arg_num = 1 or 2) Valid when your output format is "sub". If input, it will override the fps check on the input file. Ref: https://pysubs2.readthedocs.io/en/latest/api-reference.html#supported-input-output-formats (arg_num = 1) english path Project-Id-Version: 
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2020-05-06 15:57+0800
Last-Translator: 
Language-Team: 
Language: zh_CN
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.3
Plural-Forms: nplurals=1; plural=0;
 
用法：%(prog)s [-i 路径] [选项] （实验性）这个参数会取代默认的给API使用的音频声道数量。（参数个数为1）（默认参数为%(default)s） （实验性）这个参数会取代默认的给API使用的音频采样率（赫兹）。（参数个数为1）（默认参数为%(default)s） （实验性）这个参数会取代默认的给API使用的音频文件后缀。（默认参数为%(default)s） （实验性）这个参数会取代默认的音频转换命令。"[", "]" 是可选参数，可以移除。"{", "}"是必选参数，不可移除。（参数个数为1）（默认参数为%(default)s） （实验性）这个参数会取代默认的音频转换命令。相同的注意如上。（参数个数为1）（默认参数为%(default)s） 通过设置环境变量的方式添加http代理。如果参数个数是0，使用const里的代理URL。（参数个数为0或1）（const为%(const)s） 通过设置环境变量的方式添加https代理。如果参数个数是0，使用const里的代理URL。（参数个数为0或1）（const为%(const)s） 一个介于0和100之间的整数用于控制以下两个选项的匹配结果组，"-lsc"/"--list-speech-codes"以及"-ltc"/"--list-translation-codes"或者在"-bm"/"--best-match"选项中的最佳匹配结果。结果会是一组“好的匹配”，其分数需要超过这个参数的值。（参数个数为1） 音频处理选项 Auditok的选项 将Google Speech V2 API的URL改为http类型。（参数个数为0） 选择使用Speech-to-Text API。当前支持：gsv2：Google Speech V2 （https://github.com/gillesdemey/google-speech-v2）。 gcsv1：Google Cloud Speech-to-Text V1P1Beta1 （https://cloud.google.com/speech-to-text/docs）。xfyun：讯飞开放平台语音听写（流式版）WebSocket API（https://www.xfyun.cn/doc/asr/voicedictation/API.html）。baidu: 百度短语音识别/短语音识别极速版（https://ai.baidu.com/ai-doc/SPEECH/Vk38lxily）（参数个数为1）（默认参数为%(default)s） 输出字幕的格式。如果没有提供该选项，使用"-o"/"--output"参数中的后缀。如果"-o"/"--output"参数也没有提供扩展名，那么使用"{dft}"。在这种情况下，如果"-i"/"--input"的参数是一个字幕文件，那么使用和字幕文件相同的扩展名。（参数个数为1）（默认参数为{dft}） 在翻译前删除所有文本中的ass特效标签。只影响翻译结果。（参数个数为0） 删除所有没有语音识别结果的空轴。（参数个数为0） Google Speech-to-Text API用于识别可信度的回应参数。一个介于0和1之间的浮点数。可信度越高意味着结果越好。输入这个参数会导致所有低于这个结果的识别结果被删除。参考：https://github.com/BingLingGroup/google-speech-v2#response（参数个数为1）（默认参数为%(default)s） 如果不输入这个选项，它会严格控制所有语音区域的最小大小。参考：https://auditok.readthedocs.io/en/latest/core.html#class-summary（参数个数为0） 输入选项 将音频处理中产生的文件放在输出路径中。（参数个数为0） 用于语音识别的语言代码/语言标识符。推荐使用Google Cloud Speech的参考语言代码。错误的输入不会终止程序。但是后果自负。参考：https://cloud.google.com/speech-to-text/docs/languages（参数个数为1）（默认参数： %(default)s） 用于翻译的目标语言的语言代码/语言标识符。（参数个数为1）（默认参数为%(default)s） 用于翻译的目标语言的语言代码/语言标识符。如果没有提供，使用py-googletrans来自动检测源语言。（参数个数为1）（默认参数为%(default)s） 语言选项 列表选项 列出所有可用的"-SRC"/"--src-language"也就是py-googletrans可用的翻译用的语言代码。否则会给出一个“好的匹配”的清单。同样的参考文档如上。（参数个数为0或1） 列出所有可选参数。 列出所有可用的字幕文件格式。如果的你想要的格式不支持，请使用ffmpeg或者SubtitleEdit来对其进行转换。如果输出格式是"sub"且输入文件是音频无法获取到视频帧率时，你需要提供fps选项指定帧率。（参数个数为0） 列出所有推荐的"-S"/"--speech-language"Google Speech-to-Text 语言代码。如果参数没有给出，列出全部语言代码。默认的“好的匹配”标准是匹配分数超过90分（匹配分数介于0和100之间）。参考：https://tools.ietf.org/html/bcp47 https://github.com/LuminosoInsight/langcodes/blob/master/langcodes/__init__.py 语言代码范例：语言文字种类-（扩展语言文字种类）-变体（或方言）-使用区域-变体（或方言）-扩展-私有（https://www.zhihu.com/question/21980689/answer/93615123）（参数个数为0或1） 确保有空格的参数被引号包围。
默认参数指的是，
如果选项没有在命令行中提供时会使用的参数。
"参数个数"指的是如果提供了选项，
该选项所需要的参数个数。
*参数指的是那些用在选项后面的东西。*
作者: {author}
Email: {email}
问题反馈: {homepage}
 在一段有效的音频活动区域中可以容忍的最大（连续）安静区域。同样的参考文档如上。（参数个数为1）（默认参数为%(default)s） 最大音频区域大小。同样的参考文档如上。（参数个数为1）（默认参数为%(default)s） 最小语音区域大小。同样的参考文档如上。（参数个数为1）（默认参数为%(default)s） 网络选项 用于Speech-to-Text请求的并行数量。（参数个数为1）（默认参数为%(default)s） 用于ffmpeg音频切割的进程并行数量。（参数个数为1）（默认参数为%(default)s） 控制音频处理的选项。如果没有提供选项，进行正常的格式转换工作。"y"：它会先预处理输入文件，如果成功了，在语音转文字之前不会对音频进行额外的处理。"o"：只会预处理输入音频。（"-k"/"--keep"选项自动置为真）"s"：只会分割输入音频。（"-k"/"--keep"选项自动置为真）以下是用于处理音频的默认命令：{dft_1} | {dft_2} | {dft_3}（参考：https://github.com/stevenj/autosub/blob/master/scripts/subgen.sh https://ffmpeg.org/ffmpeg-filters.html）（参数个数介于1和2之间） 不使用外部语音区域控制时，用于控制Auditok的选项。 控制音频处理的选项。 控制输入的选项。 控制语言的选项。 控制网络的选项。 控制输出的选项。 控制语音转文字的选项。 控制字幕转换的选项。 其他选项 控制其他东西的选项。 输出选项 输出更多的文件。可选种类：regions，src，full-src，dst，bilingual，dst-lf-src，src-lf-dst，all。（时间轴，源语言字幕，完整语音识别结果，目标语言字幕，双语字幕，dst-lf-src,，src-lf-dst，所有）full-src：由语音转文字API得到的json格式的完整语音识别结果加上开始和结束时间。dst-lf-src：目标语言和源语言在同一字幕行中，且目标语言先于源语言。src-lf-dst：源语言和目标语言在同一字幕行中，且源语言先于目标语言。（参数个数在6和1之间）（默认参数为%(default)s） 提供外部语音区域（时间轴）的字幕文件。该字幕文件格式需要是pysubs2所支持的。使用后会替换掉默认的自动寻找语音区域（时间轴）的功能。（参数个数为1） 避免任何暂停和覆写文件的行为。如果参数有误，会直接停止程序。（参数个数为0） 参考：https://auditok.readthedocs.io/en/latest/core.html#class-summary（参数个数为0） 将指定字符替换为空格，并消除每句末尾空格。只会影响翻译结果。（参数个数为0或1）（const为%(const)s） 设置代理密码。（参数个数为1） 设置代理用户名。（参数个数为1） 设置服务账号密钥的环境变量。应该是包含服务帐号凭据的JSON文件的文件路径。如果使用了，会被API密钥选项覆盖。参考：https://cloud.google.com/docs/authentication/getting-started 当前支持：gcsv1（GOOGLE_APPLICATION_CREDENTIALS）（参数个数为1） 显示%(prog)s的帮助信息并退出。（参数个数为0） 显示%(prog)s的版本信息并退出。（参数个数为0） 语音选项 字幕转换选项 Google Speech-to-Text API的密钥。（参数个数为1）当前支持：gsv2：gsv2的API密钥。（默认参数为免费API密钥）gcsv1：gcsv1的API密钥。（如果使用了，可以覆盖 "-sa"/"--service-account"提供的服务账号凭据） 用于检测是否是语音区域的能量水平。参考：https://auditok.readthedocs.io/en/latest/apitutorial.html#examples-using-real-audio-data（参数个数为1）（默认参数为%(default)s） 输出字幕文件的路径。（默认值是"input"路径和适当的文件名后缀的结合）（参数个数为1） 用于生成字幕文件的视频/音频/字幕文件。如果输入文件是字幕文件，程序仅会对其进行翻译。（参数个数为1） 这个参数会取代默认的音频预处理命令。每行命令需要放在一个引号内。输入文件名写为{in_}。输出文件名写为{out_}。（参数个数大于1） 使用语音转文字识别配置文件来发送请求。取代以下选项："-S", "-asr", "-asf"。目前支持：gcsv1：Google Cloud Speech-to-Text V1P1Beta1 API密钥配置参考：https://cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig 服务账号配置参考：https://googleapis.dev/python/speech/latest/gapic/v1/types.html#google.cloud.speech_v1.types.RecognitionConfig 。xfyun：讯飞开放平台语音听写（流式版）WebSocket API（https://console.xfyun.cn/services/iat）。baidu: 百度短语音识别/短语音识别极速版（https://ai.baidu.com/ai-doc/SPEECH/ek38lxj1u）。如果参数个数是0，使用const路径。（参数个数为0或1）（const为%(const)s） 使用langcodes为输入获取一个最佳匹配的语言代码。仅在使用py-googletrans和Google Speech V2时起作用。如果langcodes未安装，使用fuzzywuzzy来替代。可选的模式：s, src, d, all。"s"指"-S"/"--speech-language"。"src"指"-SRC"/"--src-language"。"d"指"-D"/"--dst-language"。（参数个数在1到3之间） 使用py-googletrans去检测一个字幕文件的第一行的语言。并列出一个和该语言匹配的推荐Google Speech-to-Text语言代码清单（"-S"/"--speech-language"选项所用到的）。参考：https://cloud.google.com/speech-to-text/docs/languages（参数个数为1）（默认参数 %(default)s） 当输出格式为"ass"/"ssa"且"-sty"/"--styles"选项提供参数时有效。给输出字幕文件行提供"ass"/"ssa"字幕的样式名。如果不提供该选项，字幕行会使用文件中的第一个样式名。如果参数个数为1，字幕行会使用来自"-sty"/"--styles"的参数作为样式名。如果参数个数为2，源语言字幕行会使用第一个参数作为样式名。目标语言行使用第二个。（参数个数为1或2） 当输出格式为"sub"时有效。如果提供了该参数，它会取代原有的对输入文件的帧率检查。参考：https://pysubs2.readthedocs.io/en/latest/api-reference.html#supported-input-output-formats（参数个数为1） traditional-chinese 路径 