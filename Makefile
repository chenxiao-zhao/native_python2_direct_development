VERSION = 2.2
BUILD_DATE =`date  +%Y%m%d%H%M%S`

INSTALL_NAME = native_python2_direct_development
INSTALL_DIR = native_python2_direct_development
INSTALL_PATH = /opt/personal/${INSTALL_DIR}/
TEMP_DIR = release${INSTALL_PATH}

all:
	make package
	make deb
package:
	sed -i "s#__BUILD_DATE__#${BUILD_DATE}#g" src/main.py
	sed -i "s#__BUILD_VERSION__#${VERSION}#g" src/main.py
	cd ./src && pyinstaller -F main.py -n ${INSTALL_DIR} --runtime-tmpdir /opt/personal/work
	if [ ! -d "${TEMP_DIR}" ]; then \
		mkdir -p ${TEMP_DIR}; \
	fi
	mv ./src/dist/${INSTALL_DIR} ${TEMP_DIR}
	cp -rf conf/* ${TEMP_DIR}
	cp -rf script ${TEMP_DIR}
rpm:
	fpm -s dir -t rpm -v ${VERSION} -n ${INSTALL_NAME} --vendor "personal" --description "personal" -C ./release
	rm -rf "${TEMP_DIR}"
deb:
	fpm -s dir -t deb -v ${VERSION} -n ${INSTALL_NAME} --vendor "personal" --description "personal" --pre-install ${TEMP_DIR}/script/pre_install_ubuntu.sh --post-install ${TEMP_DIR}/script/install_ubuntu.sh --before-remove ${TEMP_DIR}/script/pre_uninstall_ubuntu.sh -C ./release
	rm -rf ./release
clean:
	sed -i "s/^.*BUILD_DATE = .*/BUILD_DATE = '__BUILD_DATE__'/" src/main.py
	sed -i "s/^.*BUILD_VERSION = .*/BUILD_VERSION = '__BUILD_VERSION__'/" src/main.py
	rm -rf ./src/dist
	rm -rf ./src/build
	rm -rf release
	rm ./src/${INSTALL_DIR}.spec
	rm *.deb