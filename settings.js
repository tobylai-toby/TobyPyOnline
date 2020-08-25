window.onload = function() {
	var el = document.getElementById("editor");
	var Myeditor = CodeMirror.fromTextArea(el, {
		mode: "python", // 语言模式
		theme: "monokai", // 主题
		keyMap: "sublime", // 快键键风格
		lineNumbers: true, // 显示行号
		smartIndent: true, // 智能缩进
		indentUnit: 4, // 智能缩进单位为4个空格长度
		indentWithTabs: true, // 使用制表符进行智能缩进
		lineWrapping: true, // 
		// 在行槽中添加行号显示器、折叠器、语法检测器
		gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter", "CodeMirror-lint-markers"],
		foldGutter: true, // 启用行槽中的代码折叠
		autofocus: true, // 自动聚焦
		matchBrackets: true, // 匹配结束符号，比如"]、}"
		autoCloseBrackets: true, // 自动闭合符号
		styleActiveLine: true, // 显示选中行的样式
	});
	// 设置初始文本，这个选项也可以在fromTextArea中配置
	var button = document.getElementById('run');
	button.onclick = function() {
		var prog = Myeditor.getValue();
		if (prog) {
			var Turtlecanvas = document.getElementById('canvas-map')
			Turtlecanvas.innerHTML =
				`<div id="canvas-map" class="mdui-color-white">
						<div class="mdui-valign">
						  <p class="mdui-center">一片空白，等你写代码</p>
						</div>
					</div>`;
			var mypre = document.getElementById("output");
			mypre.innerHTML = '';
			Sk.pre = "output";
			Sk.configure({
				output: outf,
				read: builtinRead,
				__future__: Sk.python3
			});

			(Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas-map';
			var myPromise = Sk.misceval.asyncToPromise(function() {
				return Sk.importMainWithBody("TobyPyOnline", false, prog, true);
			});

			myPromise.then(function(mod) {
					console.log('success');
				},
				function(err) {
					outerr(err.toString());
				});
		} else {
			var mypre = document.getElementById("output");
			mypre.innerHTML = '';
			var Turtlecanvas = document.getElementById('canvas-map')
			Turtlecanvas.innerHTML =
				`<div id="canvas-map" class="mdui-color-white">
						<div class="mdui-valign">
						  <p class="mdui-center">一片空白，等你写代码</p>
						</div>
					</div>`;
		}
	}
	document.onkeydown = function(e) {
		e = e || window.event;
		if (e.ctrlKey && e.keyCode == 66) { //快捷键 ctrl +B
			var prog = Myeditor.getValue();
			if (prog) {
				var Turtlecanvas = document.getElementById('canvas-map')
				Turtlecanvas.innerHTML =
					`<div id="canvas-map" class="mdui-color-white">
							<div class="mdui-valign">
							  <p class="mdui-center">一片空白，等你写代码</p>
							</div>
						</div>`;
				var mypre = document.getElementById("output");
				mypre.innerHTML = '';
				Sk.pre = "output";
				Sk.configure({
					output: outf,
					read: builtinRead,
					__future__: Sk.python3
				});

				(Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas-map';
				var myPromise = Sk.misceval.asyncToPromise(function() {
					return Sk.importMainWithBody("TobyPyOnline", false, prog, true);
				});

				myPromise.then(function(mod) {
						console.log('success');
					},
					function(err) {
						outerr(err.toString());
					});
			} else {
				var mypre = document.getElementById("output");
				mypre.innerHTML = '';
				var Turtlecanvas = document.getElementById('canvas-map')
				Turtlecanvas.innerHTML =
					`<div id="canvas-map" class="mdui-color-white">
							<div class="mdui-valign">
							  <p class="mdui-center">一片空白，等你写代码</p>
							</div>
						</div>`;
			}

			return;
		}
	};

}

function outf(text) {
	var mypre = document.getElementById("output");
	mypre.innerText = mypre.innerText + text;
}

function outerr(err) {
	var mypre = document.getElementById("output");
	err2 = err.replace('not yet implemented in Skulpt', 'not yet implemented in TobyPyOnline')
	var err_code = `<p style="color:red;">${err2}</p>`
	mypre.innerHTML = mypre.innerHTML + err_code;
}

function builtinRead(x) {
	if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
		throw "File not found: '" + x + "'";
	return Sk.builtinFiles["files"][x];
}
