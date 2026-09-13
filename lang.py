import os
import sys
import json
import shutil


class LanguageManager:
    """Manages UI translation files.

    Language files are simple JSON files placed next to the application
    (inside the "Lang" folder). Users can add their own language files:
    simply copy an existing one, translate it and it will show up in the
    Settings tab automatically.
    """

    def __init__(self):
        self._lang_dir = None
        self._strings = {}
        self._default = {}
        self._fallback = None
        self._lang_id = "en"
        self._bundled_dir = self._bundled_dir_path()
        self._ensure_lang_dir()
        self.load("en", force=True)

    def _bundled_dir_path(self):
        base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, "Lang")

    def _app_dir(self):
        if getattr(sys, "frozen", False):
            return os.path.dirname(os.path.abspath(sys.executable))
        return os.path.dirname(os.path.abspath(__file__))

    def _ensure_lang_dir(self):
        candidate = os.path.join(self._app_dir(), "Lang")
        try:
            os.makedirs(candidate, exist_ok=True)
            self._lang_dir = candidate
        except Exception:
            self._lang_dir = self._bundled_dir
        for fname in ("en.json", "ru.json"):
            target = os.path.join(self._lang_dir, fname)
            if not os.path.isfile(target):
                src = os.path.join(self._bundled_dir, fname)
                if os.path.isfile(src):
                    try:
                        shutil.copy2(src, target)
                    except Exception:
                        pass

    def set_fallback(self, func):
        """Optional callable used when a key is not found in any language file."""
        self._fallback = func

    def get_lang_dir(self):
        return self._lang_dir

    def get_lang_id(self):
        return self._lang_id

    @staticmethod
    def _read_json(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def get_available(self):
        """Return the list of available languages as dicts.

        Each dict contains: id, lang_name, native_name.
        """
        langs = []
        try:
            names = sorted(
                f for f in os.listdir(self._lang_dir)
                if f.lower().endswith(".json")
            )
        except Exception:
            names = []
        for fname in names:
            lang_id = os.path.splitext(os.path.basename(fname))[0]
            data = self._read_json(os.path.join(self._lang_dir, fname)) or {}
            langs.append({
                "id": lang_id,
                "lang_name": data.get("lang_name", lang_id),
                "native_name": data.get("native_name", lang_id),
            })
        return langs

    def load(self, lang_id, force=False):
        if lang_id == self._lang_id and not force:
            return
        data = self._read_json(os.path.join(self._lang_dir, "%s.json" % lang_id))
        if data is None and lang_id != "en":
            data = self._read_json(os.path.join(self._lang_dir, "en.json"))
        strings = {}
        if isinstance(data, dict):
            raw = data.get("strings", {})
            strings = raw if isinstance(raw, dict) else {}
        self._strings = strings
        self._lang_id = lang_id
        if lang_id == "en":
            self._default = self._strings
        elif not self._default:
            en_data = self._read_json(os.path.join(self._lang_dir, "en.json")) or {}
            en_strings = en_data.get("strings", {})
            self._default = en_strings if isinstance(en_strings, dict) else {}

    def tr(self, key):
        s = self._strings.get(key)
        if s is None:
            s = self._default.get(key)
        if s is None and self._fallback is not None:
            try:
                v = self._fallback(key)
            except Exception:
                v = None
            s = v if isinstance(v, str) else None
        return s if isinstance(s, str) else key


_instance = LanguageManager()


def get_manager():
    return _instance


def tr(key):
    return _instance.tr(key)