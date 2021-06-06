#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines autosub's command line options.
"""
# Import built-in modules
from __future__ import absolute_import, print_function, unicode_literals
import argparse
import gettext
import sys

# Import third-party modules
from googletrans import constants as gt_constants
from gooey import Gooey, GooeyParser
from gooey.python_bindings.gooey_decorator import IGNORE_COMMAND

# Any changes to the path and your own modules
from autosub import metadata
from autosub import constants

OPTIONS_TEXT = gettext.translation(domain=__name__,
                                   localedir=constants.LOCALE_PATH,
                                   languages=[constants.CURRENT_LOCALE],
                                   fallback=True)

META_TEXT = gettext.translation(domain=metadata.__name__,
                                localedir=constants.LOCALE_PATH,
                                languages=[constants.CURRENT_LOCALE],
                                fallback=True)

_ = OPTIONS_TEXT.gettext
M_ = META_TEXT.gettext


@Gooey(
    program_name=f'{metadata.NAME} {metadata.VERSION}',
    tabbed_groups=True,
    default_size=(800, 600),
    disable_progress_bar_animation=True,
)
def get_cmd_parser():  # pylint: disable=too-many-statements
    """
    Get command-line parser.
    """

    cli_mode = IGNORE_COMMAND in sys.argv
    def add_argument(group, *args, **kwargs):
        gooey_options = kwargs.get('gooey_options', {})
        if not gooey_options or gooey_options.get('show_help') is None:
            gooey_options['show_help'] = False
        kwargs['gooey_options'] = gooey_options

        group.add_argument(*args, **kwargs)

    parser = GooeyParser(
        prog=metadata.NAME,
        usage=_('\n  %(prog)s [-i path] [options]'),
        description=M_(metadata.DESCRIPTION),
        epilog=_("Make sure the argument with space is in quotes.\n"
                 "The default value is used\n"
                 "when the option is not given at the command line.\n"
                 "\"(arg_num)\" means if the option is given,\n"
                 "the number of the arguments is required.\n"
                 "Arguments *ARE* the things given behind the options.\n"
                 "Author: {author}\n"
                 "Email: {email}\n"
                 "Bug report: {homepage}\n").format(
                     author=metadata.AUTHOR,
                     email=metadata.AUTHOR_EMAIL,
                     homepage=metadata.HOMEPAGE),
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    input_group = parser.add_argument_group(
        _('Input Options'),
        _('Options to control input.'))
    lang_group = parser.add_argument_group(
        _('Language Options'),
        _('Options to control language.'))
    output_group = parser.add_argument_group(
        _('Output Options'),
        _('Options to control output.'))
    speech_group = parser.add_argument_group(
        _('Speech Options'),
        _('Options to control speech-to-text. '
          'If Speech Options not given, it will only generate the times.'))
    trans_group = parser.add_argument_group(
        _('Translation Options'),
        _('Options to control translation.'))
    conversion_group = parser.add_argument_group(
        _('Subtitles Conversion Options'),
        _('Options to control subtitles conversions.(Experimental)'))
    network_group = parser.add_argument_group(
        _('Network Options'),
        _('Options to control network.'))
    options_group = parser.add_argument_group(
        _('Other Options'),
        _('Other options to control.'))
    audio_prcs_group = parser.add_argument_group(
        _('Audio Processing Options'),
        _('Options to control audio processing.'))
    auditok_group = parser.add_argument_group(
        _('Auditok Options'),
        _('Options to control Auditok '
          'when not using external speech regions control.'))
    list_group = parser.add_argument_group(
        _('List Options'),
        _('List all available arguments.'))

    add_argument(input_group,
        '-i', '--input',
        widget='FileChooser',
        metavar=_('Video/Audio/Subtitles Path'),
        help=_("The path to the video/audio/subtitles file "
               "that needs to generate subtitles. "
               "When it is a subtitles file, "
               "the program will only translate it. "
               "(arg_num = 1)"),
        gooey_options={'full_width': True})

    add_argument(input_group,
        '-er', '--ext-regions',
        widget='FileChooser',
        metavar=_('External Speech Regions'),
        help=_("Path to the subtitles file "
               "which provides external speech regions, "
               "which is one of the formats that pysubs2 supports "
               "and overrides the default method to find speech regions. "
               "(arg_num = 1)"),
        gooey_options={'full_width': True})

    add_argument(input_group,
        '-sty', '--styles',
        nargs='?', metavar=_('Styles'),
        const=' ',
        help=_("Valid when your output format is \"ass\"/\"ssa\". "
               "Path to the subtitles file "
               "which provides \"ass\"/\"ssa\" styles for your output. "
               "If the arg_num is 0, "
               "it will use the styles from the : "
               "\"-er\"/\"--external-speech-regions\". "
               "More info on \"-sn\"/\"--styles-name\". "
               "(arg_num = 0 or 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(input_group,
        '-sn', '--style-name',
        nargs='*', metavar=_('Style Name'),
        help=_("Valid when your output format is \"ass\"/\"ssa\" "
               "and \"-sty\"/\"--styles\" is given. "
               "Adds \"ass\"/\"ssa\" styles to your events. "
               "If not provided, events will use the first one "
               "from the file. "
               "If the arg_num is 1, events will use the "
               "specific style from the arg of \"-sty\"/\"--styles\". "
               "If the arg_num is 2, src language events use the first. "
               "Dst language events use the second. "
               "(arg_num = 1 or 2)"),
        gooey_options={'visible': cli_mode})

    add_argument(lang_group,
        '-S', '--speech-language',
        widget='FilterableDropdown',
        metavar=_('Speech Langauge'),
        choices=constants.SPEECH_TO_TEXT_LANGUAGE_CODES.keys(),
        help=_("Lang code/Lang tag for speech-to-text. "
               "Recommend using the Google Cloud Speech reference "
               "lang codes. "
               "WRONG INPUT WON'T STOP RUNNING. "
               "But use it at your own risk. "
               "Ref: https://cloud.google.com/speech-to-text/docs/languages"
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(lang_group,
        '-SRC', '--src-language',
        metavar=_('Source Langauge'),
        default='auto',
        help=_("Lang code/Lang tag for translation source language. "
               "If not given, use py-googletrans to auto-detect the src language. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(lang_group,
        '-D', '--dst-language',
        metavar=_('Destination Language'),
        help=_("Lang code/Lang tag for translation destination language. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(lang_group,
        '-bm', '--best-match',
        metavar=_('Best Match'),
        nargs="*",
        help=_("Use langcodes to get a best matching lang code "
               "when your input is wrong. "
               "Only functional for py-googletrans and Google Speech API. "
               "If langcodes not installed, use fuzzywuzzy instead. "
               "Available modes: "
               "s, src, d, all. "
               "\"s\" for \"-S\"/\"--speech-language\". "
               "\"src\" for \"-SRC\"/\"--src-language\". "
               "\"d\" for \"-D\"/\"--dst-language\". "
               "(3 >= arg_num >= 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(lang_group,
        '-mns', '--min-score',
        metavar='Minimum Score',
        type=int,
        help=_("An integer between 0 and 100 "
               "to control the good match group of "
               "\"-lsc\"/\"--list-speech-codes\" "
               "or \"-ltc\"/\"--list-translation-codes\" "
               "or the match result in \"-bm\"/\"--best-match\". "
               "Result will be a group of \"good match\" "
               "whose score is above this arg. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(output_group,
        '-o', '--output',
        widget='FileSaver',
        metavar=_('Output Path'),
        help=_("The output path for subtitles file. "
               "(default: the \"input\" path combined "
               "with the proper name tails) (arg_num = 1)"))

    add_argument(output_group,
        '-F', '--format',
        metavar=_('Format'),
        help=_("Destination subtitles format. "
               "If not provided, use the extension "
               "in the \"-o\"/\"--output\" arg. "
               "If \"-o\"/\"--output\" arg doesn't provide "
               "the extension name, use \"{dft}\" instead. "
               "In this case, if \"-i\"/\"--input\" arg is a subtitles file, "
               "use the same extension from the subtitles file. "
               "(arg_num = 1) (default: {dft})").format(
                   dft=constants.DEFAULT_SUBTITLES_FORMAT),
        gooey_options={'visible': cli_mode})

    add_argument(output_group,
        '-y', '--yes',
        action='store_true',
        help=_("Prevent pauses and allow files to be overwritten. "
               "Stop the program when your args are wrong. (arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(output_group,
        '-of', '--output-files',
        widget='Listbox',
        metavar=_('Output Files'),
        nargs='*',
        default=["dst", ],
        choices=['regions', 'src', 'full-src', 'dst', 'bilingual', 'dst-lf-src', 'src-lf-dst'],
        help=_("Output more files. "
               "Available types: "
               "regions, src, full-src, dst, bilingual, dst-lf-src, src-lf-dst, all. "
               "\"regions\", \"src\", \"full-src\" are available only "
               "if input is not a subtitles file. "
               "full-src: Full result received from Speech-to-Text API in json format "
               "with start and end time. "
               "dst-lf-src: dst language and src language in the same event. "
               "And dst is ahead of src. "
               "src-lf-dst: src language and dst language in the same event. "
               "And src is ahead of dst. "
               "(6 >= arg_num >= 1) (default: %(default)s)"))

    add_argument(output_group,
        '-fps', '--sub-fps',
        metavar='Sub FPS',
        type=float,
        help=_("Valid when your output format is \"sub\". "
               "If input, it will override the fps check "
               "on the input file. "
               "Ref: https://pysubs2.readthedocs.io/en/latest/api-reference.html"
               "#supported-input-output-formats "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(speech_group,
        '-sapi', '--speech-api',
        widget='FilterableDropdown',
        metavar=_('Speech API'),
        default='gsv2',
        choices=["gsv2", "gcsv1", "xfyun", "baidu"],
        help=_("Choose which Speech-to-Text API to use. "
               "Currently support: "
               "gsv2: Google Speech V2 (https://github.com/gillesdemey/google-speech-v2). "
               "gcsv1: Google Cloud Speech-to-Text V1P1Beta1 "
               "(https://cloud.google.com/speech-to-text/docs). "
               "xfyun: Xun Fei Yun Speech-to-Text WebSocket API "
               "(https://www.xfyun.cn/doc/asr/voicedictation/API.html). "
               "baidu: Baidu Automatic Speech Recognition API "
               "(https://ai.baidu.com/ai-doc/SPEECH/Vk38lxily) "
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(speech_group,
        '-skey', '--speech-key',
        widget='PasswordField',
        metavar='Google Speech API Key',
        help=_("The API key for Google Speech-to-Text API. (arg_num = 1) "
               "Currently support: "
               "gsv2: The API key for gsv2. (default: Free API key) "
               "gcsv1: The API key for gcsv1. "
               "(If used, override the credentials "
               "given by\"-sa\"/\"--service-account\")"))

    add_argument(speech_group,
        '-sconf', '--speech-config',
        nargs='?', metavar=_('Speech Config'),
        const='config.json',
        help=_("Use Speech-to-Text recognition config file to send request. "
               "Override these options below: "
               "\"-S\", \"-asr\", \"-asf\". "
               "Currently support: "
               "gcsv1: Google Cloud Speech-to-Text V1P1Beta1 "
               "API key config reference: "
               "https://cloud.google.com/speech-to-text/docs"
               "/reference/rest/v1p1beta1/RecognitionConfig "
               "Service account config reference: "
               "https://googleapis.dev/python/speech/latest"
               "/gapic/v1/types.html"
               "#google.cloud.speech_v1.types.RecognitionConfig "
               "xfyun: Xun Fei Yun Speech-to-Text WebSocket API "
               "(https://console.xfyun.cn/services/iat). "
               "baidu: Baidu Automatic Speech Recognition API "
               "(https://ai.baidu.com/ai-doc/SPEECH/ek38lxj1u). "
               "If arg_num is 0, use const path. "
               "(arg_num = 0 or 1) (const: %(const)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(speech_group,
        '-mnc', '--min-confidence',
        widget='DecimalField',
        metavar='Minimum Confidence',
        type=float,
        default=0.0,
        help=_("Google Speech-to-Text API response for text confidence. "
               "A float value between 0 and 1. "
               "Confidence bigger means the result is better. "
               "Input this argument will drop any result below it. "
               "Ref: https://github.com/BingLingGroup/google-speech-v2#response "
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(speech_group,
        '-der', '--drop-empty-regions',
        action='store_true',
        help=_("Drop any regions without speech recognition result. "
               "(arg_num = 0)"))

    add_argument(speech_group,
        '-sc', '--speech-concurrency',
        metavar='Speech Concurrency',
        type=int,
        default=constants.DEFAULT_CONCURRENCY,
        help=_("Number of concurrent Speech-to-Text requests to make. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-tapi', '--translation-api',
        metavar=_('Translation API'),
        default='pygt',
        choices=["pygt", "man"],
        help=_("Choose which translation API to use. "
               "Currently support: "
               "pygt: py-googletrans (https://py-googletrans.readthedocs.io/en/latest/). "
               "man: Manually translate the content by write a txt or docx file and then read it. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-tf', '--translation-format',
        metavar=_('Format'),
        default='docx',
        choices=["docx", "txt"],
        help=_("Choose which output format for manual translation to use. "
               "Currently support: docx, txt. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-mts', '--max-trans-size',
        metavar='Maximum Translation Size',
        type=int,
        default=constants.DEFAULT_SIZE_PER_TRANS,
        help=_("(Experimental)Max size per translation request. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-slp', '--sleep-seconds',
        metavar=_('Sleep Seconds'),
        type=float,
        default=constants.DEFAULT_SLEEP_SECONDS,
        help=_("(Experimental)Seconds for py-googletrans to sleep "
               "between two translation requests. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-surl', '--service-urls',
        metavar='Translation URL',
        default=["translate.google.com"],
        nargs='*',
        help=_("(Experimental)Customize py-googletrans request urls. "
               "Ref: https://py-googletrans.readthedocs.io/en/latest/ "
               "(arg_num >= 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-ua', '--user-agent',
        metavar='User-Agent Headers',
        default=gt_constants.DEFAULT_USER_AGENT,
        help=_("(Experimental)Customize py-googletrans User-Agent headers. "
               "Same docs above. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-doc', '--drop-override-codes',
        action='store_true',
        help=_("Drop any .ass override codes in the text before translation. "
               "Only affect the translation result. "
               "(arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(trans_group,
        '-tdc', '--trans-delete-chars',
        nargs='?', metavar='Delete Chars after Translation',
        const="，。！",
        help=_("Replace the specific chars with a space after translation, "
               "and strip the space at the end of each sentence. "
               "Only affect the translation result. "
               "(arg_num = 0 or 1) (const: %(const)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-mjs', '--max-join-size',
        metavar='Maximum Join Size',
        type=int,
        default=constants.DEFAULT_MAX_SIZE_PER_EVENT,
        help=_("(Experimental)Max length to join two events. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-mdt', '--max-delta-time',
        metavar=_('Maximum Delta Time'),
        type=float,
        default=constants.DEFAULT_CONTINUOUS_SILENCE,
        help=_("(Experimental)Max delta time to join two events. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-dms', '--delimiters',
        metavar=_('Delimiters'),
        default=constants.DEFAULT_EVENT_DELIMITERS,
        help=_("(Experimental)Delimiters not to join two events. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-sw1', '--stop-words-1',
        metavar=_('Stop Words Set 1'),
        help=_("(Experimental)First set of Stop words to split two events. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-sw2', '--stop-words-2',
        metavar=_('Stop Words Set 2'),
        help=_("(Experimental)Second set of Stop words to split two events. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-ds', '--dont-split',
        action='store_true',
        help=_("(Experimental)Don't split. Just merge. "
               "(arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(conversion_group,
        '-jctl', '--join-control',
        metavar=_('Join Control'),
        nargs='*',
        help=_("Control the way to join and split subtitles' events. "
               "Key tag choice: [\"\\k\", \"\\ko\", \"\\kf\", (None)] (default: None). "
               "Events manual adjustment: [\"man\", \"ext-auto\", "
               "\"punct-auto\"] (default: man). "
               "You can choose \"man\" and one \"*-auto\" method at the same time "
               "which allows you to automatically adjust events at first "
               "and then manually adjust them. "
               "Capitalized the first word and add a full stop: [\"cap\", (None)] (default: None). "
               "Trim regions after processing: [\"trim\", (None)] (default: None). "
               "(arg_num >= 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(network_group,
        '-hsa', '--http-speech-api',
        action='store_true',
        help=_("Change the Google Speech V2 API "
               "URL into the http one. "
               "(arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(network_group,
        '-hsp', '--https-proxy',
        nargs='?', metavar='HTTPs Proxy URL',
        const='https://127.0.0.1:1080',
        help=_("Add https proxy by setting environment variables. "
               "If arg_num is 0, use const proxy url. "
               "(arg_num = 0 or 1) (const: %(const)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(network_group,
        '-hp', '--http-proxy',
        nargs='?', metavar='HTTP Proxy URL',
        const='http://127.0.0.1:1080',
        help=_("Add http proxy by setting environment variables. "
               "If arg_num is 0, use const proxy url. "
               "(arg_num = 0 or 1) (const: %(const)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(network_group,
        '-pu', '--proxy-username',
        metavar=_('Proxy Username'),
        help=_("Set proxy username. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(network_group,
        '-pp', '--proxy-password',
        metavar=_('Proxy Password'),
        help=_("Set proxy password. "
               "(arg_num = 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(options_group,
        '-h', '--help',
        action='help',
        help=_("Show %(prog)s help message and exit. (arg_num = 0)"))

    add_argument(options_group,
        '-V', '--version',
        action='version',
        version='%(prog)s ' + metadata.VERSION
        + ' by ' + metadata.AUTHOR + ' <'
        + metadata.AUTHOR_EMAIL + '>',
        help=_("Show %(prog)s version and exit. (arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(options_group,
        '-sa', '--service-account',
        widget='FileChooser',
        metavar=_('Service Account Path'),
        help=_("Set service account key environment variable. "
               "It should be the file path of the JSON file "
               "that contains your service account credentials. "
               "Can be overridden by the API key. "
               "Ref: https://cloud.google.com/docs/authentication/getting-started "
               "Currently support: gcsv1 (GOOGLE_APPLICATION_CREDENTIALS) "
               "(arg_num = 1)"))

    add_argument(audio_prcs_group,
        '-ap', '--audio-process',
        nargs='*', metavar=_('Audio Process'),
        help=_("Option to control audio process. "
               "If not given the option, "
               "do normal conversion work. "
               "\"y\": pre-process the input first "
               "then start normal workflow. "
               "If succeed, no more conversion before "
               "the speech-to-text procedure. "
               "\"o\": only pre-process the input audio. "
               "(\"-k\"/\"--keep\" is true) "
               "\"s\": only split the input audio. "
               "(\"-k\"/\"--keep\" is true) "
               "Default command to pre-process the audio: "
               "{dft_1} | {dft_2} | {dft_3} "
               "(Ref: "
               "https://github.com/stevenj/autosub/blob/master/scripts/subgen.sh "
               "https://ffmpeg.org/ffmpeg-filters.html) "
               "(2 >= arg_num >= 1)").format(
                   dft_1=constants.DEFAULT_AUDIO_PRCS_CMDS[0],
                   dft_2=constants.DEFAULT_AUDIO_PRCS_CMDS[1],
                   dft_3=constants.DEFAULT_AUDIO_PRCS_CMDS[2]),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-k', '--keep',
        action='store_true',
        help=_("Keep audio processing files to the output path. "
               "(arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-apc', '--audio-process-cmd',
        nargs='*', metavar=_('Command'),
        help=_("This arg will override the default "
               "audio pre-process command. "
               "Every line of the commands need to be in quotes. "
               "Input file name is {in_}. "
               "Output file name is {out_}. "
               "(arg_num >= 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-ac', '--audio-concurrency',
        metavar='Audio Concurrency',
        type=int,
        default=constants.DEFAULT_CONCURRENCY,
        help=_("Number of concurrent ffmpeg audio split process to make. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-acc', '--audio-conversion-cmd',
        metavar=_('Conversion Command'),
        default=constants.DEFAULT_AUDIO_CVT_CMD,
        help=_("(Experimental)This arg will override the default "
               "audio conversion command. "
               "\"[\", \"]\" are optional arguments "
               "meaning you can remove them. "
               "\"{\", \"}\" are required arguments "
               "meaning you can't remove them. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-asc', '--audio-split-cmd',
        metavar=_('Split Command'),
        default=constants.DEFAULT_AUDIO_SPLT_CMD,
        help=_("(Experimental)This arg will override the default "
               "audio split command. "
               "Same attention above. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-asf', '--api-suffix',
        metavar=_('File Suffix'),
        default='.flac',
        help=_("(Experimental)This arg will override the default "
               "API audio suffix. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-asr', '--api-sample-rate',
        metavar=_('Sample Rate'),
        type=int,
        default=44100,
        help=_("(Experimental)This arg will override the default "
               "API audio sample rate(Hz). "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(audio_prcs_group,
        '-aac', '--api-audio-channel',
        metavar=_('Number of Channels'),
        type=int,
        default=1,
        help=_("(Experimental)This arg will override the default "
               "API audio channel. "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    add_argument(auditok_group,
        '-et', '--energy-threshold',
        widget='Slider',
        metavar=_('Energy Threshold'),
        type=int,
        default=constants.DEFAULT_ENERGY_THRESHOLD,
        help=_("The energy level which determines the region to be detected. "
               "Ref: https://auditok.readthedocs.io/en/latest/apitutorial.html"
               "#examples-using-real-audio-data "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'min': 0, 'max': 100})

    add_argument(auditok_group,
        '-mnrs', '--min-region-size',
        widget='DecimalField',
        metavar=_('Minimum Region Size'),
        type=float,
        default=constants.DEFAULT_MIN_REGION_SIZE,
        help=_("Minimum region size. "
               "Same docs above. "
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(auditok_group,
        '-mxrs', '--max-region-size',
        widget='DecimalField',
        metavar=_('Maximum Region Size'),
        type=float,
        default=constants.DEFAULT_MAX_REGION_SIZE,
        help=_("Maximum region size. "
               "Same docs above. "
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(auditok_group,
        '-mxcs', '--max-continuous-silence',
        widget='DecimalField',
        metavar=_('Maximum Continuous Silence'),
        type=float,
        default=constants.DEFAULT_CONTINUOUS_SILENCE,
        help=_("Maximum length of a tolerated silence within a valid audio activity. "
               "Same docs above. "
               "(arg_num = 1) (default: %(default)s)"))

    add_argument(auditok_group,
        '-nsml', '--not-strict-min-length',
        action='store_true',
        help=_("If not input this option, "
               "it will keep all regions strictly follow the minimum region limit. "
               "Ref: https://auditok.readthedocs.io/en/latest/core.html#class-summary "
               "(arg_num = 0)"))

    add_argument(auditok_group,
        '-dts', '--drop-trailing-silence',
        action='store_true',
        help=_("Ref: https://auditok.readthedocs.io/en/latest/core.html#class-summary "
               "(arg_num = 0)"))

    add_argument(auditok_group,
        '-aconf', '--auditok-config',
        nargs='?', metavar=_('Auditok Config Path'),
        const='aconfig.json',
        help=_("Auditok options automatic optimization config."
               "(arg_num = 0 or 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(list_group,
        '-lf', '--list-formats',
        action='store_true',
        help=_("List all available subtitles formats. "
               "If your format is not supported, "
               "you can use ffmpeg or SubtitleEdit to convert the formats. "
               "You need to offer fps option "
               "when input is an audio file "
               "and output is \"sub\" format. "
               "(arg_num = 0)"),
        gooey_options={'visible': cli_mode})

    add_argument(list_group,
        '-lsc', '--list-speech-codes',
        metavar=_('Speech Codes'),
        const=' ',
        nargs='?',
        help=_("List all recommended \"-S\"/\"--speech-language\" "
               "Google Speech-to-Text language codes. "
               "If no arg is given, list all. "
               "Or else will list a group of \"good match\" "
               "of the arg. Default \"good match\" standard is whose "
               "match score above 90 (score between 0 and 100). "
               "Ref: https://tools.ietf.org/html/bcp47 "
               "https://github.com/LuminosoInsight/langcodes/blob/master/langcodes/__init__.py "
               "lang code example: language-script-region-variant-extension-privateuse "
               "(arg_num = 0 or 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(list_group,
        '-ltc', '--list-translation-codes',
        metavar=_('Translation Codes'),
        const=' ',
        nargs='?',
        help=_("List all available \"-SRC\"/\"--src-language\" "
               "py-googletrans translation language codes. "
               "Or else will list a group of \"good match\" "
               "of the arg. "
               "Same docs above. "
               "(arg_num = 0 or 1)"),
        gooey_options={'visible': cli_mode})

    add_argument(list_group,
        '-dsl', '--detect-sub-language',
        metavar=_('path'),
        help=_("Use py-googletrans to detect a sub file's first line language. "
               "And list a group of matched language in recommended "
               "\"-S\"/\"--speech-language\" Google Speech-to-Text language codes. "
               "Ref: https://cloud.google.com/speech-to-text/docs/languages "
               "(arg_num = 1) (default: %(default)s)"),
        gooey_options={'visible': cli_mode})

    return parser
