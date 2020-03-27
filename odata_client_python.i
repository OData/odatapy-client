%module odata_client_python

%define SHAREDPTR(type)
%shared_ptr(:: ## type)
%shared_ptr(type)
%enddef

%{

#include <locale>
#include "odata/core/odata_json_constants.h"
#include "odata/edm/edm_model_utility.h"
#include "odata/client/odata_client.h" 

%} 

%include <std_except.i>
%include <std_string.i>
%include <std_vector.i>
%include <std_shared_ptr.i>

%include <exception.i>

%include <pycontainer.swg>

namespace web {
    namespace http {
        typedef unsigned short status_code;
    }
}

SHAREDPTR(odata::edm::edm_named_type)
SHAREDPTR(odata::edm::edm_primitive_type)
SHAREDPTR(odata::edm::edm_property_type)
SHAREDPTR(odata::edm::edm_collection_type)
SHAREDPTR(odata::edm::edm_payload_annotation_type)
SHAREDPTR(odata::edm::edm_structured_type)
SHAREDPTR(odata::edm::edm_enum_type)
SHAREDPTR(odata::edm::edm_complex_type)
SHAREDPTR(odata::edm::edm_navigation_type)
SHAREDPTR(odata::edm::edm_operation_type)
SHAREDPTR(odata::edm::edm_entity_type)

SHAREDPTR(odata::edm::edm_model)
SHAREDPTR(odata::edm::edm_schema)
SHAREDPTR(odata::edm::edm_entity_container)
SHAREDPTR(odata::edm::edm_operation_parameter)
SHAREDPTR(odata::edm::edm_enum_member)
SHAREDPTR(odata::edm::edm_entity_set)
SHAREDPTR(odata::edm::edm_navigation_source)
SHAREDPTR(odata::edm::edm_singleton)
SHAREDPTR(odata::edm::edm_operation_import)

SHAREDPTR(odata::core::odata_entity_value)
SHAREDPTR(odata::core::odata_structured_value)
SHAREDPTR(odata::core::odata_value)
SHAREDPTR(odata::core::odata_primitive_value)
SHAREDPTR(odata::core::odata_structured_value)
SHAREDPTR(odata::core::odata_collection_value)
SHAREDPTR(odata::core::odata_enum_value)
SHAREDPTR(odata::core::odata_complex_value)

%include "cpprest/details/basic_types.h"

namespace utility {
    class datetime {
        public:
            enum date_format {
                RFC_1123,
                ISO_8601
            };
            static datetime utc_now();
            static datetime from_string(const utility::string_t& timestring, date_format format);
            utility::string_t to_string(date_format format) const;
    };
/* TODO: fix seconds?
    class seconds {
        public:


    }
*/
}

%include "odata/edm/edm_type.h"
%include "odata/edm/edm_navigation_source.h"
%include "odata/edm/edm_entity_set.h"
%include "odata/edm/edm_singleton.h"
%include "odata/edm/edm_operation_import.h"
%include "odata/edm/edm_entity_container.h"
%include "odata/edm/edm_schema.h"
%include "odata/edm/edm_model.h"
%include "odata/edm/edm_model_utility.h"

%include "odata/core/odata_json_constants.h"
%include "odata/core/odata_value.h"

namespace odata {
    namespace core {
        class odata_property_map;
    }
}

%include "odata/core/odata_primitive_value.h"
%include "odata/core/odata_structured_value.h"
%include "odata/core/odata_collection_value.h"
%include "odata/core/odata_entity_value.h"
%include "odata/core/odata_enum_value.h"
%include "odata/core/odata_complex_value.h"
%include "odata/core/odata_parameter.h"
%include "odata/core/odata_entity_model_builder.h"

%include "odata/communication/http_service_exception.h"
%include "odata/communication/http_communication.h"

%include "odata/client/odata_client_options.h"

%exception odata::client::odata_client::send_data_to_server {
  try {
    $action
  } catch (odata::communication::service_exception &e) {
    std::string msg = utility::conversions::scan_string(e.what());
    SWIG_exception(SWIG_RuntimeError, msg.c_str());
  } catch (std::invalid_argument &e) {
    SWIG_exception(SWIG_AttributeError, e.what());
  } catch (std::exception &e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  } 
}

%include "odata/client/odata_client.h"

%extend odata::edm::edm_entity_container {
    std::vector< std::shared_ptr< ::odata::edm::edm_operation_import >,std::allocator< std::shared_ptr< ::odata::edm::edm_operation_import > > > get_operation_import_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_operation_import> > ret;
        auto operation_imports = self->get_operation_imports();
        for (const auto &it : operation_imports)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_singleton >,std::allocator< std::shared_ptr< ::odata::edm::edm_singleton > > > get_singleton_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_singleton> > ret;
        auto singletons = self->get_singletons();
        for (const auto &it : singletons)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_entity_set >,std::allocator< std::shared_ptr< ::odata::edm::edm_entity_set > > > get_entity_set_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_entity_set> > ret;
        for (auto it = self->begin(); it != self->end(); ++it)
            ret.push_back(it->second);
        return ret;
    }
}

%extend odata::edm::edm_schema {
    std::vector< std::shared_ptr< ::odata::edm::edm_entity_type >,std::allocator< std::shared_ptr< ::odata::edm::edm_entity_type > > > get_entity_types_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_entity_type> > ret;
        auto entity_types = self->get_entity_types();
        for (const auto &it : entity_types)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_complex_type >,std::allocator< std::shared_ptr< ::odata::edm::edm_complex_type > > > get_complex_types_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_complex_type> > ret;
        auto complex_types = self->get_complex_types();
        for (const auto &it : complex_types)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_enum_type >,std::allocator< std::shared_ptr< ::odata::edm::edm_enum_type > > > get_enum_types_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_enum_type> > ret;
        auto enum_types = self->get_enum_types();
        for (const auto &it : enum_types)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_operation_type >,std::allocator< std::shared_ptr< ::odata::edm::edm_operation_type > > > get_operation_types_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_operation_type> > ret;
        auto operation_types = self->get_operation_types();
        for (const auto &it : operation_types)
            ret.push_back(it.second);
        return ret;
    }

    std::vector< std::shared_ptr< ::odata::edm::edm_entity_container >,std::allocator< std::shared_ptr< ::odata::edm::edm_entity_container > > > get_containers_vector() const {
        std::vector< std::shared_ptr<::odata::edm::edm_entity_container> > ret;
        auto entity_containers = self->get_containers();
        for (const auto &it : entity_containers)
            ret.push_back(it.second);
        return ret;
    }
}

namespace pplx {
 template<class _ReturnType>
 class task {
    public:
   _ReturnType get() const;
 };
}

%exception pplx::task::get {
  try {
    $action
  } catch (odata::communication::service_exception &e) {
    std::string msg = utility::conversions::scan_string(e.what());
    SWIG_exception(SWIG_RuntimeError, msg.c_str());
  } catch (std::exception &e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
}

%template(task_edm_model) pplx::task< std::shared_ptr< ::odata::edm::edm_model > >;
%template(task_odata_entity_values) pplx::task< std::vector< std::shared_ptr< ::odata::core::odata_entity_value > > >;
%template(task_odata_values) pplx::task< std::vector< std::shared_ptr< ::odata::core::odata_value > > >;
%template(task_http_status_code) pplx::task< ::web::http::status_code >;


%template(vector_string_t) std::vector< ::utility::string_t >;
%template(vector_odata_value) std::vector< std::shared_ptr< ::odata::core::odata_value > >;
%template(vector_odata_entity_value) std::vector< std::shared_ptr< ::odata::core::odata_entity_value > >;
%template(vector_odata_parameter) std::vector< std::shared_ptr< ::odata::core::odata_parameter > >;
%template(vector_edm_schema) std::vector< std::shared_ptr< ::odata::edm::edm_schema > >;
%template(vector_edm_operation_parameter) std::vector< std::shared_ptr< ::odata::edm::edm_operation_parameter > >;
%template(vector_edm_enum_member) std::vector< std::shared_ptr< ::odata::edm::edm_enum_member > >;
%template(vector_edm_entity_type) std::vector< std::shared_ptr< ::odata::edm::edm_entity_type > >;
%template(vector_edm_complex_type) std::vector< std::shared_ptr< ::odata::edm::edm_complex_type > >;
%template(vector_edm_enum_type) std::vector< std::shared_ptr< ::odata::edm::edm_enum_type > >;
%template(vector_edm_operation_type) std::vector< std::shared_ptr< ::odata::edm::edm_operation_type > >;
%template(vector_edm_entity_container) std::vector< std::shared_ptr< ::odata::edm::edm_entity_container > >;
%template(vector_edm_property_type) std::vector< std::shared_ptr< ::odata::edm::edm_property_type > >;
%template(vector_edm_entity_set) std::vector< std::shared_ptr< ::odata::edm::edm_entity_set > >;
%template(vector_edm_singleton) std::vector< std::shared_ptr< ::odata::edm::edm_singleton > >;
%template(vector_edm_operation_import) std::vector< std::shared_ptr< ::odata::edm::edm_operation_import > >;


%inline {

	std::shared_ptr<::odata::core::odata_primitive_value> to_primitive_value(std::shared_ptr<odata::core::odata_value> org_value) {
		return std::dynamic_pointer_cast<odata::core::odata_primitive_value>(org_value);
	}

	std::shared_ptr<::odata::core::odata_collection_value> to_collection_value(std::shared_ptr<odata::core::odata_value> org_value) {
		return std::dynamic_pointer_cast<odata::core::odata_collection_value>(org_value);
	}

	std::shared_ptr<::odata::core::odata_complex_value> to_complex_value(std::shared_ptr<odata::core::odata_value> org_value) {
		return std::dynamic_pointer_cast<odata::core::odata_complex_value>(org_value);
	}

	std::shared_ptr<::odata::core::odata_entity_value> to_entity_value(std::shared_ptr<odata::core::odata_value> org_value) {
		return std::dynamic_pointer_cast<odata::core::odata_entity_value>(org_value);
	}

	std::shared_ptr<::odata::core::odata_enum_value> to_enum_value(std::shared_ptr<odata::core::odata_value> org_value) {
		return std::dynamic_pointer_cast<odata::core::odata_enum_value>(org_value);
	}

	std::shared_ptr<::odata::edm::edm_primitive_type> to_primitive_type(std::shared_ptr<odata::edm::edm_named_type> org_type) {
		return std::dynamic_pointer_cast<odata::edm::edm_primitive_type>(org_type);
	}

	std::shared_ptr<::odata::edm::edm_navigation_type> to_navigation_type(std::shared_ptr<odata::edm::edm_named_type> org_type) {
		return std::dynamic_pointer_cast<odata::edm::edm_navigation_type>(org_type);
	}

	std::shared_ptr<::odata::edm::edm_collection_type> to_collection_type(std::shared_ptr<odata::edm::edm_named_type> org_type) {
		return std::dynamic_pointer_cast<odata::edm::edm_collection_type>(org_type);
	}

	std::shared_ptr<::odata::edm::edm_entity_type> to_entity_type(std::shared_ptr<odata::edm::edm_named_type> org_type) {
		return std::dynamic_pointer_cast<odata::edm::edm_entity_type>(org_type);
	}

	std::shared_ptr<::odata::edm::edm_complex_type> to_complex_type(std::shared_ptr<odata::edm::edm_named_type> org_type) {
		return std::dynamic_pointer_cast<odata::edm::edm_complex_type>(org_type);
	}

	bool is_nullptr(std::shared_ptr<odata::core::odata_value> ptr) {
		return ptr == nullptr;
	}

	::utility::seconds to_duration(long long time) {
		return ::utility::seconds(time);
	}
}
