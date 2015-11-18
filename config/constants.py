# This file contains values used throughout the codebase.
# Don't change values if you don't know what they do.

ALLOWED_EXTENSIONS = set(['csv', 'json', 'mp4', 'txt'])
FILE_TYPES = ['gps', 'accel', 'voiceRecording', 'powerState', 'callLog', 'textLog',
              'bluetoothLog', 'surveyAnswers', 'surveyTimings']

#TODO: Eli/Josh. These values are still used in the graph, which needs to be rewritten anyway
DAILY_SURVEY_NAME = 'Daily'
WEEKLY_SURVEY_NAME = 'Weekly'

#Survey types
SURVEY_TYPES = ['audio_survey', 'tracking_survey']

CHECKBOX_TOGGLES = ["accelerometer",
                  "gps",
                  "calls",
                  "texts",
                  "wifi",
                  "bluetooth",
                  "power_state"]

TIMER_VALUES = ["accelerometer_off_duration_seconds",
                "accelerometer_on_duration_seconds",
                "bluetooth_on_duration_seconds",
                "bluetooth_total_duration_seconds",
                "bluetooth_global_offset_seconds", 
                "check_for_new_surveys_frequency_seconds",
                "create_new_data_files_frequency_seconds",
                "gps_off_duration_seconds",
                "gps_on_duration_seconds",
                "seconds_before_auto_logout",
                "upload_data_files_frequency_seconds",
                "voice_recording_max_time_length_seconds",
                "wifi_log_frequency_seconds"]

CONCURRENT_NETWORK_OPS = 10

API_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
"""1990-01-31T07:30:04 gets you jan 31 1990 at 7:30:04am
   human string is YYYY-MM-DDThh:mm:ss """
CHUNK_TIMESLICE_QUANTUM = 3600

HUMAN_READABLE_TIME_LABEL = ",UTC time"

CHUNKS_FOLDER = "CHUNKED_DATA"

ACCELEROMETER = "accelerometer"
BLUETOOTH = "bluetooth"
CALL_LOG = "calls"
GPS = "gps"
IDENTIFIERS = "identifiers"
LOG_FILE = "app_log"
POWER_STATE = "power_state"
SURVEY_ANSWERS = "survey_answers"
SURVEY_TIMINGS = "survey_timings"
TEXTS_LOG = "texts"
VOICE_RECORDING = "audio_recordings"
WIFI = "wifi"

ALL_DATA_STREAMS = [ACCELEROMETER, BLUETOOTH, CALL_LOG, GPS, IDENTIFIERS,
                    LOG_FILE, POWER_STATE, SURVEY_ANSWERS, SURVEY_TIMINGS,
                    TEXTS_LOG, VOICE_RECORDING, WIFI]
CHUNKABLE_FILES = set( [ACCELEROMETER, BLUETOOTH, CALL_LOG, GPS, IDENTIFIERS,
                  LOG_FILE, POWER_STATE, SURVEY_TIMINGS, TEXTS_LOG, WIFI] )
# RAW_FILES = set([SURVEY_ANSWERS, VOICE_RECORDING, LOG_FILE ])

# each chunk represents 1 hour of data, and because unix time 0 is on an hour
# boundry our time codes will also be on nice, clean hour boundaries.

LENGTH_OF_STUDY_ID = 24
