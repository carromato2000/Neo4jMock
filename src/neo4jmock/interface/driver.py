from .session import Session

class Driver:
    def execute_query(self,
                      query,
                      parameters_ = None,
                      routing_ = None,
                      database_ = None,
                      impersonated_user_ = None,
                      auth_ = None,
                      result_transformer_ = None,
                      **kwargs):
        self._encrypted = kwargs.get("encrypted", False)

    @property
    def encrypted(self):
        return self._encrypted

    def session(self,
                **config):
        return Session()

    def close(self):
        raise NotImplementedError()

    def verify_connectivity(self, 
                            **config):
        raise NotImplementedError()

    def get_server_info(self,
                        **config):
        raise NotImplementedError()

    def supports_multi_db(self):
        return True

    def verify_authentication(self, 
                              auth = None, 
                              **config):
        raise NotImplementedError()

    def supports_session_auth(self):
        raise NotImplementedError()

class GraphDatabase:
    @classmethod
    def driver(cls, 
               uri, 
               auth = None, 
               **config):
        raise NotImplementedError()

    @classmethod
    def bookmark_manager(cls, 
                         initial_bookmarks = None,
                         bookmarks_supplier = None,
                         bookmark_consumer = None
                        ):
        raise NotImplementedError()